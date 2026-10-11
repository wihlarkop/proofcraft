"""Focused tests for Proofcraft's small runtime run contract."""
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from runtime_workspace import create_run


class RuntimeWorkspaceTests(unittest.TestCase):
    def test_run_metadata_is_scoped_and_completion_is_not_a_verdict(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            run = create_run(
                root,
                "accept",
                scope={"target": "unit"},
                source_revision="abc123",
                now=datetime(2026, 10, 11, 1, 2, 3, tzinfo=timezone.utc),
                id_factory=lambda: "0123456789abcdef",
            )

            self.assertEqual(run.path, root / ".proofcraft/runs/accept/20261011T010203Z-0123456789abcdef")
            self.assertTrue(run.path.is_dir())
            self.assertTrue(run.path.resolve().is_relative_to(root.resolve()))
            self.assertEqual(run.metadata["run_id"], run.path.name)
            self.assertEqual(run.metadata["workflow"], "accept")
            self.assertEqual(run.metadata["created_at"], "2026-10-11T01:02:03Z")
            self.assertEqual(run.metadata["source_revision"], "abc123")
            self.assertEqual(run.metadata["scope"], {"target": "unit"})
            self.assertEqual(run.metadata["status"], "running")
            self.assertFalse((run.path / "report.md").exists())

            run.update(status="completed")
            metadata = json.loads((run.path / "run.json").read_text(encoding="utf-8"))
            self.assertEqual(metadata["status"], "completed")
            self.assertNotIn("verdict", metadata)
            self.assertNotIn("incomplete_reason", metadata)

            incomplete = create_run(root, "debug", scope={})
            incomplete.update(status="incomplete", incomplete_reason="reproduction timed out")
            metadata = json.loads((incomplete.path / "run.json").read_text(encoding="utf-8"))
            self.assertEqual(metadata["status"], "incomplete")
            self.assertEqual(metadata["incomplete_reason"], "reproduction timed out")

    def test_run_ids_are_unique_under_concurrent_creation(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            def create(_):
                return create_run(root, "eval", scope={}).path

            with ThreadPoolExecutor(max_workers=8) as pool:
                paths = list(pool.map(create, range(24)))

            self.assertEqual(len(paths), len(set(paths)))
            self.assertTrue(all(path.parent == root / ".proofcraft/runs/eval" for path in paths))
            self.assertTrue(all((path / "run.json").is_file() for path in paths))

    def test_collision_retries_without_overwriting_an_existing_run(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            parent = root / ".proofcraft/runs/eval"
            existing = parent / "20261011T010203Z-collision"
            existing.mkdir(parents=True)
            marker = existing / "user-evidence.txt"
            marker.write_text("retain", encoding="utf-8")
            ids = iter(("collision", "fresh"))

            run = create_run(
                root,
                "eval",
                scope={},
                now=datetime(2026, 10, 11, 1, 2, 3, tzinfo=timezone.utc),
                id_factory=lambda: next(ids),
            )

            self.assertEqual(run.path.name, "20261011T010203Z-fresh")
            self.assertEqual(marker.read_text(encoding="utf-8"), "retain")

    def test_initial_metadata_write_failure_removes_only_the_new_partial_run(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            parent = root / ".proofcraft/runs/eval"
            existing = parent / "20261011T010203Z-collision"
            existing.mkdir(parents=True)
            marker = existing / "user-evidence.txt"
            marker.write_text("retain", encoding="utf-8")
            unrelated = parent / "unrelated.txt"
            unrelated.write_text("preserve", encoding="utf-8")
            failed_path = parent / "20261011T010203Z-fresh"
            ids = iter(("collision", "fresh"))
            failure = OSError("injected initial metadata write failure")
            original_open = Path.open

            class PartialWriteFailure:
                def __init__(self, stream):
                    self.stream = stream

                def __enter__(self):
                    return self

                def __exit__(self, *args):
                    return self.stream.__exit__(*args)

                def write(self, value):
                    self.stream.write(value[:8])
                    raise failure

            def open_with_partial_run_json(path, mode="r", *args, **kwargs):
                stream = original_open(path, mode, *args, **kwargs)
                if path == failed_path / "run.json" and mode == "x":
                    return PartialWriteFailure(stream)
                return stream

            with patch.object(Path, "open", autospec=True, side_effect=open_with_partial_run_json):
                with self.assertRaises(OSError) as raised:
                    create_run(
                        root,
                        "eval",
                        scope={},
                        now=datetime(2026, 10, 11, 1, 2, 3, tzinfo=timezone.utc),
                        id_factory=lambda: next(ids),
                    )

            self.assertIs(raised.exception, failure)
            self.assertFalse(failed_path.exists())
            self.assertEqual(marker.read_text(encoding="utf-8"), "retain")
            self.assertEqual(unrelated.read_text(encoding="utf-8"), "preserve")
            self.assertEqual(set(parent.iterdir()), {existing, unrelated})

    def test_workflow_cannot_escape_the_runtime_parent(self):
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(ValueError):
                create_run(Path(td), "../outside", scope={})

    def test_permission_error_is_propagated_without_replacement(self):
        with tempfile.TemporaryDirectory() as td:
            denied = PermissionError("access denied")
            with patch.object(Path, "mkdir", side_effect=denied):
                with self.assertRaises(PermissionError) as raised:
                    create_run(Path(td), "eval", scope={})
            self.assertIs(raised.exception, denied)

    def test_runtime_parent_symlink_is_rejected_without_writing_through_it(self):
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as outside:
            link = Path(td) / ".proofcraft"
            try:
                os.symlink(outside, link, target_is_directory=True)
            except (OSError, NotImplementedError) as error:
                self.skipTest(f"directory symlinks unavailable: {error}")

            with self.assertRaisesRegex(OSError, "linked runtime directory"):
                create_run(Path(td), "eval", scope={})
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_non_directory_runtime_parent_preserves_the_filesystem_error(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            parent = root / ".proofcraft"
            parent.write_text("user file", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                create_run(root, "eval", scope={})
            self.assertEqual(parent.read_text(encoding="utf-8"), "user file")


if __name__ == "__main__":
    unittest.main()
