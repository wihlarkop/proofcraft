"""Architecture and case-selection contracts for the security-audit workflow."""
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SecurityAuditWorkflowTests(unittest.TestCase):
    def test_security_audit_is_core_while_review_and_security_specialist_keep_ownership(self):
        suite = json.loads((ROOT / "suite.yaml").read_text(encoding="utf-8"))
        core = suite["skills"]["core"]
        domain = suite["skills"]["domain"]

        self.assertEqual(len(core), 12)
        self.assertEqual(len(suite["implemented"]), 26)
        self.assertIn("security-audit", core)
        self.assertNotIn("security-audit", domain)
        self.assertIn("review", core)
        self.assertIn("security-engineering", domain)

    def test_evaluation_cases_cover_audit_contract_and_negative_review_routing(self):
        data = json.loads(
            (ROOT / "src/skills/security-audit/evals/evals.json").read_text(encoding="utf-8")
        )
        cases = {case["id"]: case for case in data["evals"]}
        required = {
            "source-boundary-violation",
            "framework-protected-false-positive",
            "deployment-dependent-hypothesis",
            "independent-verifier-unavailable",
            "untrusted-execution-boundary",
            "negative-ordinary-pr-review",
        }

        self.assertTrue(required.issubset(cases))
        self.assertFalse(cases["negative-ordinary-pr-review"]["should_trigger"])
        self.assertTrue(
            all(cases[case_id]["should_trigger"] for case_id in required - {"negative-ordinary-pr-review"})
        )


if __name__ == "__main__":
    unittest.main()
