"""Safety and selection checks; no Node, model, or credentials required."""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("eval_runner", ROOT / "scripts/eval.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class EvalSetupTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
