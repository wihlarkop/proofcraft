#!/usr/bin/env python3
"""Validate portable Proofcraft security-audit evidence without executing target code."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
import re
import stat
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any


FINDING_STATES = {"confirmed", "needs_validation", "rejected"}
AUDIT_STATUSES = {"complete", "incomplete", "blocked"}
ASSESSMENTS = {"findings_present", "no_confirmed_findings", "not_determined"}
LIFECYCLE_STATUSES = {"running", "completed", "incomplete"}
COVERAGE_STATUSES = {"examined", "partially_examined", "blocked", "not_examined"}
SEVERITIES = {"critical", "high", "medium", "low"}
VERIFICATION_METHODS = {"separate_reviewer", "fresh_context"}
VERIFICATION_CONCLUSIONS = {"supports", "refutes", "inconclusive"}
RUN_ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*\Z")
MAX_DOCUMENT_BYTES = 8 * 1024 * 1024
MAX_JSON_NESTING = 128
MAX_DIAGNOSTICS = 100
MAX_DIAGNOSTIC_LENGTH = 512


class _Diagnostics(list[str]):
    """Keep validation output useful and bounded for hostile input documents."""

    def __init__(self) -> None:
        super().__init__()
        self._truncated = False

    def append(self, error: str) -> None:
        if len(self) < MAX_DIAGNOSTICS:
            if len(error) > MAX_DIAGNOSTIC_LENGTH:
                error = error[: MAX_DIAGNOSTIC_LENGTH - 3] + "..."
            super().append(error)
        elif not self._truncated:
            super().append(f"Further validation errors omitted after {MAX_DIAGNOSTICS} diagnostics.")
            self._truncated = True


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_link(path: Path) -> bool:
    junction_check = getattr(path, "is_junction", None)
    return path.is_symlink() or bool(junction_check and junction_check())


def _contains_link(path: Path) -> bool:
    absolute = path.absolute()
    parts = absolute.parts
    if not parts:
        return False
    current = Path(parts[0])
    if _is_link(current):
        return True
    for part in parts[1:]:
        current = current / part
        if _is_link(current):
            return True
    return False


def _windows_junction_detection_supported() -> bool:
    return not sys.platform.startswith("win") or callable(getattr(Path("."), "is_junction", None))


def _exceeds_json_nesting_limit(text: str) -> bool:
    depth = 0
    in_string = False
    escaped = False
    for character in text:
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
            continue
        if character == '"':
            in_string = True
        elif character in "[{":
            depth += 1
            if depth > MAX_JSON_NESTING:
                return True
        elif character in "]}":
            depth -= 1
    return False


def _root(value: str | Path, label: str, errors: list[str]) -> Path | None:
    path = Path(value).absolute()
    if _contains_link(path):
        errors.append(f"{label} must not contain a symlink or junction: {path}")
        return None
    try:
        mode = path.stat().st_mode
    except (OSError, ValueError) as error:
        errors.append(f"{label} is unavailable: {path}: {error}")
        return None
    if not stat.S_ISDIR(mode):
        errors.append(f"{label} is not a directory: {path}")
        return None
    return path


def _reference(value: Any, root: Path | None, label: str, errors: list[str]) -> None:
    if not _text(value):
        errors.append(f"{label} must be a non-empty relative path")
        return
    reference = value.strip()
    posix = PurePosixPath(reference)
    windows = PureWindowsPath(reference)
    if (
        "\\" in reference
        or "\x00" in reference
        or ":" in reference
        or posix.is_absolute()
        or windows.is_absolute()
        or windows.drive
        or not posix.parts
        or any(part in {"", ".", ".."} for part in posix.parts)
    ):
        errors.append(f"{label} must be a safe root-relative path using forward slashes: {reference!r}")
        return
    if root is None:
        return
    candidate = root.joinpath(*posix.parts).absolute()
    try:
        candidate.relative_to(root)
    except ValueError:
        errors.append(f"{label} escapes its root: {reference!r}")
        return
    if _contains_link(candidate):
        errors.append(f"{label} must not follow a symlink or junction: {reference!r}")
        return
    try:
        mode = candidate.stat().st_mode
    except (OSError, ValueError) as error:
        errors.append(f"{label} is unavailable: {reference!r}: {error}")
        return
    if not stat.S_ISREG(mode):
        errors.append(f"{label} is not a regular file: {reference!r}")


def _read_json(path_value: str | Path, label: str, errors: list[str]) -> dict[str, Any] | None:
    path = Path(path_value)
    if _contains_link(path):
        errors.append(f"{label} must not be a symlink or junction: {path}")
        return None
    try:
        with path.open("rb") as source:
            raw = source.read(MAX_DOCUMENT_BYTES + 1)
    except OSError as error:
        errors.append(f"cannot read {label}: {path}: {error}")
        return None
    if len(raw) > MAX_DOCUMENT_BYTES:
        errors.append(f"{label} JSON exceeds the {MAX_DOCUMENT_BYTES // (1024 * 1024)} MiB limit: {path}")
        return None
    try:
        text = raw.decode("utf-8")
    except UnicodeError as error:
        errors.append(f"{label} is not valid UTF-8 JSON: {error}")
        return None
    if _exceeds_json_nesting_limit(text):
        errors.append(f"{label} JSON nesting exceeds the {MAX_JSON_NESTING}-level limit")
        return None
    try:
        value = json.loads(text, object_pairs_hook=_unique_object)
    except RecursionError:
        errors.append(f"{label} JSON nesting exceeds the supported parser depth")
        return None
    except ValueError as error:
        errors.append(f"cannot read {label} as JSON: {path}: {error}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label} must be a JSON object")
        return None
    return value


def _required_text(obj: dict[str, Any], key: str, label: str, errors: list[str]) -> str | None:
    value = obj.get(key)
    if not _text(value):
        errors.append(f"{label}.{key} must be a non-empty string")
        return None
    return value.strip()


def _string_list(obj: dict[str, Any], key: str, label: str, errors: list[str], *, nonempty: bool) -> list[str]:
    value = obj.get(key)
    if not isinstance(value, list) or not all(_text(item) for item in value):
        errors.append(f"{label}.{key} must be an array of non-empty strings")
        return []
    result = [item.strip() for item in value]
    if nonempty and not result:
        errors.append(f"{label}.{key} must not be empty")
    return result


def _source_location(
    finding: dict[str, Any], label: str, source_root: Path | None, errors: list[str]
) -> None:
    location = finding.get("source")
    if not isinstance(location, dict):
        errors.append(f"{label}.source must be an object")
        return
    _reference(location.get("path"), source_root, f"{label}.source.path", errors)
    start = location.get("line_start")
    end = location.get("line_end")
    if not isinstance(start, int) or isinstance(start, bool) or start < 1:
        errors.append(f"{label}.source.line_start must be a positive integer")
    if end is not None and (
        not isinstance(end, int) or isinstance(end, bool) or end < 1
    ):
        errors.append(f"{label}.source.line_end must be a positive integer")
    elif isinstance(start, int) and not isinstance(start, bool) and isinstance(end, int) and end < start:
        errors.append(f"{label}.source.line_end must not precede line_start")


def _evidence(value: Any, label: str, evidence_root: Path | None, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{label} must be a non-empty array of evidence paths")
        return
    for index, reference in enumerate(value):
        _reference(reference, evidence_root, f"{label}[{index}]", errors)


def _finding(
    value: Any,
    index: int,
    source_root: Path | None,
    evidence_root: Path | None,
    errors: list[str],
) -> tuple[str | None, str | None]:
    label = f"findings[{index}]"
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return None, None

    finding_id = _required_text(value, "id", label, errors)
    state = _required_text(value, "state", label, errors)
    for key in ("title", "vulnerability_class", "boundary"):
        _required_text(value, key, label, errors)
    _source_location(value, label, source_root, errors)
    _evidence(value.get("evidence"), f"{label}.evidence", evidence_root, errors)

    if state not in FINDING_STATES:
        errors.append(f"{label}.state must be one of {sorted(FINDING_STATES)}")
        return finding_id, state

    if state == "confirmed":
        _string_list(value, "preconditions", label, errors, nonempty=True)
        _required_text(value, "path_summary", label, errors)
        _required_text(value, "impact", label, errors)
        _required_text(value, "remediation", label, errors)
        severity = value.get("severity")
        if not isinstance(severity, dict):
            errors.append(f"{label}.severity must be an object for a confirmed finding")
        else:
            severity_level = severity.get("level")
            if not isinstance(severity_level, str) or severity_level not in SEVERITIES:
                errors.append(f"{label}.severity.level must be one of {sorted(SEVERITIES)}")
            _required_text(severity, "rationale", f"{label}.severity", errors)

        verification = value.get("verification")
        if not isinstance(verification, dict):
            errors.append(f"{label}.verification is required for a confirmed finding")
        else:
            if verification.get("status") != "independently_verified":
                errors.append(f"{label}.verification.status must be independently_verified")
            _required_text(verification, "verifier", f"{label}.verification", errors)
            verification_method = verification.get("method")
            if not isinstance(verification_method, str) or verification_method not in VERIFICATION_METHODS:
                errors.append(f"{label}.verification.method must be one of {sorted(VERIFICATION_METHODS)}")
            discovery = _required_text(verification, "discovery_context", f"{label}.verification", errors)
            verification_context = _required_text(
                verification, "verification_context", f"{label}.verification", errors
            )
            if discovery and verification_context and discovery == verification_context:
                errors.append(f"{label}.verification contexts must be distinct")
            _required_text(verification, "falsification_attempt", f"{label}.verification", errors)
            _required_text(verification, "result", f"{label}.verification", errors)
            conclusion = _required_text(verification, "conclusion", f"{label}.verification", errors)
            if conclusion and conclusion not in VERIFICATION_CONCLUSIONS:
                errors.append(
                    f"{label}.verification.conclusion must be one of {sorted(VERIFICATION_CONCLUSIONS)}"
                )
            elif conclusion and conclusion != "supports":
                errors.append(f"{label}.verification.conclusion must be supports for a confirmed finding")
            _evidence(
                verification.get("evidence"),
                f"{label}.verification.evidence",
                evidence_root,
                errors,
            )
    elif state == "needs_validation":
        if "severity" in value:
            errors.append(f"{label}.severity is not allowed for needs_validation")
        verification = value.get("verification")
        if isinstance(verification, dict) and verification.get("conclusion") == "refutes":
            errors.append(f"{label}.state must be rejected when verification.conclusion is refutes")
        _required_text(value, "hypothesis", label, errors)
        _string_list(value, "unresolved_facts", label, errors, nonempty=True)
        _string_list(value, "validation_steps", label, errors, nonempty=True)
    else:
        if "severity" in value:
            errors.append(f"{label}.severity is not allowed for rejected candidates")
        _required_text(value, "rejection_reason", label, errors)

    return finding_id, state


def _coverage(
    value: Any,
    source_identity: str | None,
    scope: str | None,
    source_root: Path | None,
    evidence_root: Path | None,
    finding_ids: set[str],
    audit_status: str | None,
    errors: list[str],
) -> None:
    if not isinstance(value, dict):
        return
    if type(value.get("schema_version")) is not int or value.get("schema_version") != 1:
        errors.append("coverage.schema_version must be 1")
    ledger_identity = _required_text(value, "source_identity", "coverage", errors)
    ledger_scope = _required_text(value, "scope", "coverage", errors)
    if source_identity and ledger_identity and source_identity != ledger_identity:
        errors.append("findings and coverage source_identity values must match")
    if scope and ledger_scope and scope != ledger_scope:
        errors.append("findings and coverage scope values must match")

    required_ids = _string_list(value, "required_unit_ids", "coverage", errors, nonempty=True)
    if len(required_ids) != len(set(required_ids)):
        errors.append("coverage.required_unit_ids must be unique")
    units = value.get("units")
    if not isinstance(units, list):
        errors.append("coverage.units must be an array")
        return

    unit_map: dict[str, dict[str, Any]] = {}
    covered_finding_ids: set[str] = set()
    for index, unit in enumerate(units):
        label = f"coverage.units[{index}]"
        if not isinstance(unit, dict):
            errors.append(f"{label} must be an object")
            continue
        unit_id = _required_text(unit, "id", label, errors)
        _required_text(unit, "boundary", label, errors)
        status = _required_text(unit, "status", label, errors)
        if unit_id:
            if unit_id in unit_map:
                errors.append(f"duplicate coverage unit id: {unit_id}")
            else:
                unit_map[unit_id] = unit
        if status not in COVERAGE_STATUSES:
            errors.append(f"{label}.status must be one of {sorted(COVERAGE_STATUSES)}")
            continue
        observations = _string_list(unit, "observations", label, errors, nonempty=False)
        source_paths = _string_list(unit, "source_paths", label, errors, nonempty=False)
        evidence = unit.get("evidence", [])
        if not isinstance(evidence, list) or not all(_text(item) for item in evidence):
            errors.append(f"{label}.evidence must be an array of non-empty strings")
            evidence = []
        finding_refs = _string_list(unit, "finding_ids", label, errors, nonempty=False)
        for source_index, reference in enumerate(source_paths):
            _reference(reference, source_root, f"{label}.source_paths[{source_index}]", errors)
        for evidence_index, reference in enumerate(evidence):
            _reference(reference, evidence_root, f"{label}.evidence[{evidence_index}]", errors)
        for finding_ref in finding_refs:
            covered_finding_ids.add(finding_ref)
            if finding_ref not in finding_ids:
                errors.append(f"{label} references missing finding id: {finding_ref}")
        if status in {"examined", "partially_examined"} and not observations:
            errors.append(f"{label}.observations are required for {status} coverage")
        if status == "examined" and not source_paths and not evidence:
            errors.append(f"{label} needs source_paths or evidence when examined")
        if status != "examined" and not _text(unit.get("gap")):
            errors.append(f"{label}.gap is required when coverage is {status}")

    for finding_id in finding_ids - covered_finding_ids:
        errors.append(f"finding is not linked to a coverage unit: {finding_id}")

    for required_id in required_ids:
        unit = unit_map.get(required_id)
        if unit is None:
            errors.append(f"required coverage unit is missing: {required_id}")
        elif audit_status == "complete" and unit.get("status") != "examined":
            errors.append(f"complete audit has unexamined required coverage unit: {required_id}")


def _run_metadata(path: str | Path | None, errors: list[str]) -> dict[str, Any] | None:
    if path is None:
        return None
    run = _read_json(path, "run metadata", errors)
    if run is None:
        return None
    if run.get("workflow") != "security-audit":
        errors.append("run metadata.workflow must be security-audit")
    lifecycle_status = run.get("status")
    if not isinstance(lifecycle_status, str) or lifecycle_status not in LIFECYCLE_STATUSES:
        errors.append(f"run metadata.status must be one of {sorted(LIFECYCLE_STATUSES)}")
    run_id = _required_text(run, "run_id", "run metadata", errors)
    if run_id and not RUN_ID_PATTERN.fullmatch(run_id):
        errors.append("run metadata.run_id must use portable letters, digits, or hyphens")
    created_at = _required_text(run, "created_at", "run metadata", errors)
    if created_at:
        try:
            timestamp = datetime.fromisoformat(
                created_at[:-1] + "+00:00" if created_at.endswith("Z") else created_at
            )
        except ValueError:
            errors.append("run metadata.created_at must be an ISO 8601 timestamp with a timezone")
        else:
            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                errors.append("run metadata.created_at must include a timezone")
    run_scope = run.get("scope")
    if not isinstance(run_scope, dict):
        errors.append("run metadata.scope must be an object")
    else:
        _required_text(run_scope, "target", "run metadata.scope", errors)
    if "source_revision" in run and not _text(run.get("source_revision")):
        errors.append("run metadata.source_revision must be a non-empty string when supplied")
    if "incomplete_reason" in run and not _text(run.get("incomplete_reason")):
        errors.append("run metadata.incomplete_reason must be a non-empty string when supplied")
    for key in ("verdict", "audit_status", "assessment", "finding_state"):
        if key in run:
            errors.append(f"run metadata must keep {key} outside lifecycle metadata")
    return run


def validate_bundle(
    findings_path: str | Path,
    coverage_path: str | Path,
    source_root: str | Path,
    evidence_root: str | Path,
    run_metadata_path: str | Path | None = None,
) -> list[str]:
    """Return structural errors for an audit bundle; never imports or executes target files."""
    errors = _Diagnostics()
    if not _windows_junction_detection_supported():
        errors.append("Windows path validation requires Python 3.12+ for reliable junction detection")
        return errors
    findings_source_root = _root(source_root, "source root", errors)
    findings_evidence_root = _root(evidence_root, "evidence root", errors)
    findings = _read_json(findings_path, "findings", errors)
    coverage = _read_json(coverage_path, "coverage ledger", errors)
    run_metadata = _run_metadata(run_metadata_path, errors)

    if findings is None:
        return errors
    if type(findings.get("schema_version")) is not int or findings.get("schema_version") != 1:
        errors.append("findings.schema_version must be 1")
    source_identity = _required_text(findings, "source_identity", "findings", errors)
    scope = _required_text(findings, "scope", "findings", errors)
    if run_metadata is not None:
        run_revision = run_metadata.get("source_revision")
        if _text(run_revision) and source_identity and run_revision.strip() != source_identity:
            errors.append("run metadata.source_revision must match findings.source_identity")
        run_scope = run_metadata.get("scope")
        if isinstance(run_scope, dict):
            run_target = run_scope.get("target")
            if _text(run_target) and scope and run_target.strip() != scope:
                errors.append("run metadata.scope.target must match findings.scope")
    audit_status = _required_text(findings, "audit_status", "findings", errors)
    assessment = _required_text(findings, "assessment", "findings", errors)
    if audit_status not in AUDIT_STATUSES:
        errors.append(f"findings.audit_status must be one of {sorted(AUDIT_STATUSES)}")
    if assessment not in ASSESSMENTS:
        errors.append(f"findings.assessment must be one of {sorted(ASSESSMENTS)}")
    candidates = findings.get("findings")
    finding_ids: set[str] = set()
    confirmed_count = 0
    if not isinstance(candidates, list):
        errors.append("findings.findings must be an array")
        candidates = []
    for index, candidate in enumerate(candidates):
        finding_id, state = _finding(
            candidate, index, findings_source_root, findings_evidence_root, errors
        )
        if finding_id:
            if finding_id in finding_ids:
                errors.append(f"duplicate finding id: {finding_id}")
            finding_ids.add(finding_id)
        if state == "confirmed":
            confirmed_count += 1

    if confirmed_count:
        expected_assessment = "findings_present"
    elif audit_status == "complete":
        expected_assessment = "no_confirmed_findings"
    else:
        expected_assessment = "not_determined"
    if assessment in ASSESSMENTS and assessment != expected_assessment:
        errors.append(
            f"findings.assessment must be {expected_assessment} for the recorded findings and audit_status"
        )

    _coverage(
        coverage,
        source_identity,
        scope,
        findings_source_root,
        findings_evidence_root,
        finding_ids,
        audit_status,
        errors,
    )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate security-audit JSON and file references without executing target code."
    )
    parser.add_argument("--findings", required=True, help="Path to findings.json")
    parser.add_argument("--coverage", required=True, help="Path to coverage-ledger.json")
    parser.add_argument("--source-root", required=True, help="Root for source-relative references")
    parser.add_argument("--evidence-root", required=True, help="Root for evidence-relative references")
    parser.add_argument("--run-metadata", help="Optional Runtime Workspace run.json")
    args = parser.parse_args(argv)

    errors = validate_bundle(
        args.findings,
        args.coverage,
        args.source_root,
        args.evidence_root,
        args.run_metadata,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Security-audit evidence is structurally valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
