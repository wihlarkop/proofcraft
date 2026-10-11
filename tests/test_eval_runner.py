"""Safety and selection checks; no Node, model, or credentials required."""
import importlib.util
import sys
import tempfile
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("eval_runner", ROOT / "scripts/eval.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class EvalSetupTests(unittest.TestCase):
    def test_fixture_git_commands_cannot_discover_parent_repository(self):
        with tempfile.TemporaryDirectory() as td:
            parent = Path(td)
            runner.initialize_fixture(parent)
            (parent / "unrelated-parent-file.txt").write_text("not eval input")
            fixture = parent / "nested-fixture"
            fixture.mkdir()
            (fixture / ".git").mkdir()  # Reproduce the ineffective marker from the interrupted run.
            (fixture / "README.md").write_text("authorized fixture")
            proof = runner.initialize_fixture(fixture)
            self.assertFalse(fixture.resolve().is_relative_to(ROOT.resolve()))
            self.assertEqual(Path(proof["git_toplevel"]).resolve(), fixture.resolve())
            self.assertEqual(proof["git_status"].strip(), "?? README.md")
            for args in (["status", "--short"], ["diff", "--name-only"],
                         ["rev-parse", "--show-toplevel"]):
                output = subprocess.check_output(
                    ["git", "-c", f"safe.directory={fixture.as_posix()}", *args],
                    cwd=fixture, text=True)
                self.assertNotIn("unrelated-parent-file", output)
                self.assertNotIn(ROOT.as_posix(), output.replace("\\", "/"))

    def test_fixture_directory_escapes_checkout_and_rejects_nested_git_boundary(self):
        external = runner.fixture_directory(ROOT / ".eval-workspace" / "boundary-test")
        try:
            self.assertFalse(external.resolve().is_relative_to(ROOT.resolve()))
            with self.assertRaisesRegex(ValueError, "outside Proofcraft"):
                runner.initialize_fixture(ROOT / ".eval-workspace" / "boundary-test")
        finally:
            external.rmdir()

    def test_comparison_uses_distinct_fixtures_and_matching_provider_filters(self):
        with tempfile.TemporaryDirectory() as td:
            config = runner.prepare(Path(td), ["shape", "improve"], ROOT / "skills", "gpt-6-sol")
            labels = {p["label"] for p in config["providers"]}
            workspaces = [Path(p["config"]["working_dir"]) for p in config["providers"]]
            self.assertEqual(len(workspaces), len(set(workspaces)))
            for provider in config["providers"]:
                settings = provider["config"]
                workspace = Path(settings["working_dir"])
                self.assertTrue((workspace / ".agents/skills/shape/SKILL.md").is_file())
                self.assertFalse((workspace / "scripts/eval.py").exists())
                self.assertFalse(list(workspace.rglob("*.pyc")))
                self.assertEqual(settings["approval_policy"], "never")
                self.assertNotIn("apiKey", settings)
                self.assertNotIn("CODEX_HOME", settings.get("cli_env", {}))
            for case in config["tests"]:
                self.assertEqual(len(case["providers"]), 2)
                self.assertTrue(set(case["providers"]) <= labels)
                self.assertTrue(any(a["type"] == "llm-rubric" for a in case["assert"]))

    def test_canonical_prompts_and_expectations_are_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            config = runner.prepare(Path(td), ["shape"], None, "gpt-6-sol")
            sources = runner.scenarios("shape")
            for case in config["tests"]:
                original = sources[case["metadata"]["scenario"]]
                self.assertEqual(case["vars"]["request"], original["prompt"])
                self.assertIn(original["expected_output"], case["assert"][-1]["value"])
                self.assertIn(original["prompt"], case["assert"][-1]["value"])

    def test_missing_baseline_skill_fails_before_model_execution(self):
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaisesRegex(ValueError, "baseline.*shape"):
                runner.prepare(Path(td) / "run", ["shape"], Path(td) / "missing", "gpt-6-sol")

    def test_response_cases_keep_canonical_rubrics_and_read_only_composition(self):
        with tempfile.TemporaryDirectory() as td:
            config = runner.prepare(Path(td), runner.SKILLS, None, "gpt-6-sol", "response-")
            expected = {
                f"{skill}:{case_id}"
                for skill in runner.SKILLS
                for case_id in runner.scenarios(skill)
                if case_id.startswith("response-")
            }
            self.assertEqual({case["description"] for case in config["tests"]}, expected)
            providers = {provider["label"]: provider for provider in config["providers"]}
            for case in config["tests"]:
                original = runner.scenarios(case["metadata"]["skill"])[case["metadata"]["scenario"]]
                self.assertEqual(case["vars"]["request"], original["prompt"])
                self.assertIn(original["expected_output"], case["assert"][-1]["value"])
                self.assertEqual(len(case["providers"]), 1)
                provider = providers[case["providers"][0]]
                self.assertEqual(provider["config"]["sandbox_mode"], "read-only")
                workspace = Path(provider["config"]["working_dir"])
                for owner in ("setup", "api-design", "implement", "improve", "review",
                              "ui-engineering", "reliability-engineering", "integration-engineering"):
                    self.assertTrue((workspace / ".agents/skills" / owner / "SKILL.md").is_file())
                contract = workspace / ".agents/skills/api-design/references/response-contract.md"
                self.assertEqual(contract.read_bytes(),
                                 (ROOT / "src/skills/api-design/references/response-contract.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
