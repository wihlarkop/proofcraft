"""Regression coverage for bytecode hygiene in generated skill output."""
import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build as build_module
import check_generated


class GeneratedPythonBytecodeTests(unittest.TestCase):
    def test_build_excludes_bytecode_at_every_depth_and_keeps_distributable_assets(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            sources = root / "src" / "skills"
            shared = root / "src" / "shared"
            skill = sources / "sample"
            skill.mkdir(parents=True)
            shared.mkdir(parents=True)
            (skill / "SOURCE.md").write_text("# Sample skill\n", encoding="utf-8")
            (skill / "validator.py").write_text("print('source')\n", encoding="utf-8")
            (skill / "case.json").write_text("{}\n", encoding="utf-8")
            (skill / "top.pyc").write_bytes(b"bytecode")
            (skill / "__pycache__" / "direct.pyc").parent.mkdir()
            (skill / "__pycache__" / "direct.pyc").write_bytes(b"bytecode")
            nested = skill / "references" / "nested"
            nested.mkdir(parents=True)
            (skill / "references" / "guide.md").write_text("Guide\n", encoding="utf-8")
            (nested / "tool.py").write_text("print('tool')\n", encoding="utf-8")
            (nested / "embedded.pyc").write_bytes(b"bytecode")
            (nested / "__pycache__" / "nested.pyc").parent.mkdir()
            (nested / "__pycache__" / "nested.pyc").write_bytes(b"bytecode")

            output = root / "skills"
            with patch.object(build_module, "SRC_SKILLS", sources), patch.object(build_module, "SHARED", shared):
                build_module.build(output)

            generated = output / "sample"
            self.assertTrue((generated / "SKILL.md").is_file())
            self.assertTrue((generated / "validator.py").is_file())
            self.assertTrue((generated / "case.json").is_file())
            self.assertTrue((generated / "references" / "guide.md").is_file())
            self.assertTrue((generated / "references" / "nested" / "tool.py").is_file())
            self.assertFalse(any(path.name == "__pycache__" for path in generated.rglob("*")))
            self.assertFalse(any(path.is_file() and path.name.endswith(".pyc") for path in generated.rglob("*")))

    def test_checker_ignores_runtime_bytecode_but_detects_real_asset_changes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            expected = root / "expected"
            current = root / "project" / "skills"
            expected_skill = expected / "sample"
            current_skill = current / "sample"
            expected_skill.mkdir(parents=True)
            current_skill.mkdir(parents=True)
            (expected_skill / "SKILL.md").write_text("# Sample\n", encoding="utf-8")
            (current_skill / "SKILL.md").write_text("# Sample\n", encoding="utf-8")
            expected_ref = expected_skill / "references" / "guide.md"
            current_ref = current_skill / "references" / "guide.md"
            expected_ref.parent.mkdir()
            current_ref.parent.mkdir()
            expected_ref.write_text("Original guide\n", encoding="utf-8")
            current_ref.write_text("Original guide\n", encoding="utf-8")
            (expected_skill / "__pycache__").mkdir()
            (expected_skill / "__pycache__" / "expected.pyc").write_bytes(b"expected cache")
            (current_skill / "__pycache__").mkdir()
            (current_skill / "__pycache__" / "runtime.pyc").write_bytes(b"runtime cache")
            (current_skill / "runtime.pyc").write_bytes(b"runtime cache")

            def build_expected(output: Path) -> None:
                shutil.copytree(expected, output)

            with patch.object(check_generated, "ROOT", root / "project"), patch.object(check_generated, "build", build_expected):
                with contextlib.redirect_stdout(io.StringIO()):
                    check_generated.main()

                current_ref.write_text("Changed legitimate reference\n", encoding="utf-8")
                output = io.StringIO()
                with contextlib.redirect_stdout(output), self.assertRaises(SystemExit) as error:
                    check_generated.main()

            self.assertEqual(error.exception.code, 1)
            self.assertIn("guide.md", output.getvalue())


if __name__ == "__main__":
    unittest.main()
