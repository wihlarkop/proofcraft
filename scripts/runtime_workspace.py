"""Minimal local runtime paths and invocation-scoped run metadata."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import errno
import json
import os
from pathlib import Path
import re
import uuid


_WORKFLOW = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
_RUN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*\Z")


def _is_link(path: Path) -> bool:
    is_junction = getattr(path, "is_junction", None)
    return path.is_symlink() or bool(is_junction and is_junction())


def _ensure_directory(path: Path) -> None:
    if _is_link(path):
        raise OSError(errno.ELOOP, "Refusing a linked runtime directory", str(path))
    try:
        path.mkdir()
    except FileExistsError:
        if _is_link(path):
            raise OSError(errno.ELOOP, "Refusing a linked runtime directory", str(path))
        if not path.is_dir():
            raise
    if _is_link(path):
        raise OSError(errno.ELOOP, "Refusing a linked runtime directory", str(path))


def ensure_runtime_directory(root: Path, *parts: str) -> Path:
    """Create a trusted runtime directory lazily, rejecting links in its path."""
    root = Path(root).resolve()
    path = root
    for part in (".proofcraft", *parts):
        if not part or part in {".", ".."} or "/" in part or "\\" in part:
            raise ValueError(f"Invalid runtime path component: {part!r}")
        path = path / part
        _ensure_directory(path)
    if not path.resolve().is_relative_to(root):
        raise ValueError(f"Runtime path escaped workspace: {path}")
    return path


@dataclass
class RunWorkspace:
    root: Path
    workflow: str
    run_id: str
    path: Path
    metadata: dict

    def update(self, *, status: str, incomplete_reason: str | None = None) -> None:
        """Persist lifecycle state without adding an acceptance verdict."""
        if status not in {"running", "completed", "incomplete"}:
            raise ValueError(f"Invalid run lifecycle status: {status}")
        if status == "incomplete" and incomplete_reason:
            self.metadata["incomplete_reason"] = incomplete_reason
        else:
            self.metadata.pop("incomplete_reason", None)
        self.metadata["status"] = status
        _write_metadata(self)


def _write_metadata(run: RunWorkspace) -> None:
    expected = run.root / ".proofcraft" / "runs" / run.workflow / run.run_id
    if run.path != expected:
        raise ValueError("Run metadata path is outside its workspace boundary")
    for directory in (run.root / ".proofcraft", run.root / ".proofcraft/runs",
                      run.root / ".proofcraft/runs" / run.workflow, run.path):
        if _is_link(directory) or not directory.is_dir():
            raise OSError(errno.ELOOP if _is_link(directory) else errno.ENOTDIR,
                          "Unsafe or missing runtime directory", str(directory))
    metadata_path = run.path / "run.json"
    if _is_link(metadata_path):
        raise OSError(errno.ELOOP, "Refusing linked run metadata", str(metadata_path))
    temporary = run.path / f".run-{uuid.uuid4().hex}.tmp"
    with temporary.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(run.metadata, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    os.replace(temporary, metadata_path)


def _cleanup_failed_allocation(path: Path, metadata_path: Path, metadata_created: bool) -> None:
    directories = (path.parent.parent.parent, path.parent.parent, path.parent, path)
    for directory in directories:
        if _is_link(directory) or not directory.is_dir():
            raise OSError(errno.ELOOP if _is_link(directory) else errno.ENOTDIR,
                          "Unsafe or missing runtime directory during cleanup", str(directory))
    if metadata_created:
        if _is_link(metadata_path):
            raise OSError(errno.ELOOP, "Refusing linked run metadata during cleanup", str(metadata_path))
        try:
            metadata_path.unlink()
        except FileNotFoundError:
            pass
    for directory in directories:
        if _is_link(directory) or not directory.is_dir():
            raise OSError(errno.ELOOP if _is_link(directory) else errno.ENOTDIR,
                          "Unsafe or missing runtime directory during cleanup", str(directory))
    path.rmdir()


def create_run(
    root: Path,
    workflow: str,
    *,
    scope: dict,
    source_revision: str | None = None,
    now: datetime | None = None,
    id_factory=None,
) -> RunWorkspace:
    """Create a unique run directory and exclusive initial run.json."""
    if not _WORKFLOW.fullmatch(workflow):
        raise ValueError(f"Invalid workflow name: {workflow!r}")
    if not isinstance(scope, dict):
        raise ValueError("Run scope must be a JSON object")
    root = Path(root).resolve()
    parent = ensure_runtime_directory(root, "runs", workflow)
    created = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    created_at = created.isoformat(timespec="seconds").replace("+00:00", "Z")
    stamp = created.strftime("%Y%m%dT%H%M%SZ")
    make_id = id_factory or (lambda: uuid.uuid4().hex[:16])

    for _ in range(32):
        token = make_id()
        if not isinstance(token, str) or not _RUN_ID.fullmatch(token):
            raise ValueError("Run ID suffix must contain only portable letters, digits, or hyphens")
        run_id = f"{stamp}-{token}"
        path = parent / run_id
        metadata = {
            "run_id": run_id,
            "workflow": workflow,
            "created_at": created_at,
            "status": "running",
            "scope": scope,
        }
        if source_revision:
            metadata["source_revision"] = source_revision
        initial_metadata = json.dumps(metadata, indent=2, ensure_ascii=False) + "\n"
        try:
            path.mkdir()
        except FileExistsError:
            continue
        metadata_path = path / "run.json"
        metadata_created = False
        try:
            with metadata_path.open("x", encoding="utf-8", newline="\n") as stream:
                metadata_created = True
                stream.write(initial_metadata)
        except BaseException as allocation_error:
            try:
                _cleanup_failed_allocation(path, metadata_path, metadata_created)
            except BaseException as cleanup_error:
                raise allocation_error from cleanup_error
            raise
        return RunWorkspace(root, workflow, run_id, path, metadata)
    raise FileExistsError(errno.EEXIST, "Could not allocate a unique run directory", str(parent))
