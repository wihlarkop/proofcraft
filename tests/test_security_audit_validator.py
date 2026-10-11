"""Behavioral checks for the portable, source-first audit evidence validator."""
import importlib.util
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "src/skills/security-audit/validate_audit.py"
SPEC = importlib.util.spec_from_file_location("security_audit_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class SecurityAuditValidatorTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source_root = self.root / "source"
        self.evidence_root = self.root / "evidence"
        self.control_root = self.root / "control"
        for directory in (self.source_root, self.evidence_root, self.control_root):
            directory.mkdir()
        (self.source_root / "service.py").write_text("def load_record():\n    pass\n", encoding="utf-8")
        (self.evidence_root / "discovery.md").write_text("Observed source path.", encoding="utf-8")
        (self.evidence_root / "independent.md").write_text(
            "Fresh-context falsification attempt.", encoding="utf-8"
        )
        self.findings = {
            "schema_version": 1,
            "source_identity": "revision-abc123",
            "scope": "tenant record read endpoint",
            "audit_status": "complete",
            "assessment": "findings_present",
            "findings": [
                {
                    "id": "SEC-001",
                    "title": "Tenant record lookup is not scoped to the principal",
                    "vulnerability_class": "broken access control",
                    "boundary": "authenticated principal to tenant-owned record",
                    "state": "confirmed",
                    "source": {"path": "service.py", "line_start": 1, "line_end": 2},
                    "preconditions": ["An authenticated user can supply another tenant identifier."],
                    "path_summary": "The request tenant identifier reaches the record lookup without an ownership check.",
                    "evidence": ["discovery.md"],
                    "impact": "A user can read another tenant's record.",
                    "remediation": "Scope the lookup to the authenticated principal's authorized tenant.",
                    "severity": {
                        "level": "high",
                        "rationale": "Cross-tenant disclosure is reachable by an authenticated user.",
                    },
                    "verification": {
                        "status": "independently_verified",
                        "verifier": "independent-reviewer",
                        "method": "fresh_context",
                        "discovery_context": "audit-pass-1",
                        "verification_context": "fresh-review-pass-1",
                        "falsification_attempt": "Looked for a server-side tenant ownership check.",
                        "conclusion": "supports",
                        "result": "No check exists before the query.",
                        "evidence": ["independent.md"],
                    },
                }
            ],
        }
        self.coverage = {
            "schema_version": 1,
            "source_identity": "revision-abc123",
            "scope": "tenant record read endpoint",
            "required_unit_ids": ["tenant-read"],
            "units": [
                {
                    "id": "tenant-read",
                    "boundary": "authenticated principal to tenant-owned record",
                    "status": "examined",
                    "observations": ["The request tenant identifier reaches the lookup."],
                    "source_paths": ["service.py"],
                    "evidence": ["discovery.md"],
                    "finding_ids": ["SEC-001"],
                }
            ],
        }
        self.run_metadata = {
            "run_id": "20261011T000000Z-0123456789abcdef",
            "workflow": "security-audit",
            "created_at": "2026-10-11T00:00:00Z",
            "status": "completed",
            "source_revision": "revision-abc123",
            "scope": {"target": "tenant record read endpoint"},
        }

    def validate(self, *, run_metadata=True):
        findings_path = self.control_root / "findings.json"
        coverage_path = self.control_root / "coverage-ledger.json"
        findings_path.write_text(json.dumps(self.findings), encoding="utf-8")
        coverage_path.write_text(json.dumps(self.coverage), encoding="utf-8")
        run_path = None
        if run_metadata:
            run_path = self.control_root / "run.json"
            run_path.write_text(json.dumps(self.run_metadata), encoding="utf-8")
        return validator.validate_bundle(
            findings_path,
            coverage_path,
            self.source_root,
            self.evidence_root,
            run_path,
        )

    def test_accepts_confirmed_finding_with_distinct_independent_verification(self):
        self.assertEqual(self.validate(), [])

    def test_confirmed_finding_requires_supportive_structured_verifier_conclusion(self):
        verification = self.findings["findings"][0]["verification"]
        self.assertEqual(self.validate(), [])

        for conclusion in ("refutes", "inconclusive"):
            verification["conclusion"] = conclusion
            errors = self.validate()
            self.assertTrue(
                any("verification.conclusion must be supports" in error for error in errors),
                errors,
            )

        verification.pop("conclusion")
        errors = self.validate()
        self.assertTrue(any("verification.conclusion must be a non-empty string" in error for error in errors), errors)

        verification["conclusion"] = "unrecognized"
        errors = self.validate()
        self.assertTrue(any("verification.conclusion must be one of" in error for error in errors), errors)

    def test_needs_validation_does_not_become_confirmed_from_verification_record(self):
        finding = self.findings["findings"][0]
        finding["state"] = "needs_validation"
        finding["hypothesis"] = "The request may permit a cross-tenant lookup."
        finding["unresolved_facts"] = ["The authorization middleware is not available."]
        finding["validation_steps"] = ["Inspect the middleware and its caller."]
        for key in ("preconditions", "path_summary", "impact", "remediation", "severity"):
            finding.pop(key)
        self.findings["assessment"] = "no_confirmed_findings"

        self.assertEqual(self.validate(), [])

    def test_refuted_candidate_uses_rejected_disposition(self):
        finding = self.findings["findings"][0]
        finding["state"] = "needs_validation"
        finding["hypothesis"] = "The request may permit a cross-tenant lookup."
        finding["unresolved_facts"] = ["The authorization middleware is not available."]
        finding["validation_steps"] = ["Inspect the middleware and its caller."]
        finding["verification"]["conclusion"] = "refutes"
        for key in ("preconditions", "path_summary", "impact", "remediation", "severity"):
            finding.pop(key)
        self.findings["assessment"] = "no_confirmed_findings"

        errors = self.validate()

        self.assertTrue(any("state must be rejected when verification.conclusion is refutes" in error for error in errors), errors)

        finding["state"] = "rejected"
        finding["rejection_reason"] = "The verifier found an ownership check before the query."
        for key in ("hypothesis", "unresolved_facts", "validation_steps"):
            finding.pop(key)
        self.assertEqual(self.validate(), [])

    def test_run_metadata_source_and_scope_match_audit_documents(self):
        self.assertEqual(self.validate(), [])

        self.run_metadata["source_revision"] = "revision-other"
        errors = self.validate()
        self.assertTrue(any("source_revision must match findings.source_identity" in error for error in errors), errors)

        self.run_metadata["source_revision"] = "revision-abc123"
        self.run_metadata["scope"]["target"] = "different audit target"
        errors = self.validate()
        self.assertTrue(any("scope.target must match findings.scope" in error for error in errors), errors)

    def test_requires_verification_context_separate_from_discovery(self):
        finding = self.findings["findings"][0]
        verification = finding.pop("verification")
        errors = self.validate()
        self.assertTrue(any(".verification is required" in error for error in errors), errors)

        finding["verification"] = verification
        verification["verification_context"] = verification["discovery_context"]

        errors = self.validate()

        self.assertTrue(any("contexts must be distinct" in error for error in errors), errors)

    def test_unresolved_hypothesis_cannot_carry_severity(self):
        finding = self.findings["findings"][0]
        finding["state"] = "needs_validation"
        finding["hypothesis"] = "A proxy may fail to add the Secure cookie attribute."
        finding["unresolved_facts"] = ["Production proxy configuration is unavailable."]
        finding["validation_steps"] = ["Inspect the deployed proxy configuration."]
        for key in ("preconditions", "path_summary", "impact", "verification"):
            finding.pop(key)
        finding["severity"] = {"level": "high", "rationale": "unresolved"}
        self.findings["audit_status"] = "incomplete"
        self.findings["assessment"] = "not_determined"
        self.coverage["units"][0]["status"] = "partially_examined"
        self.coverage["units"][0]["gap"] = "Deployment configuration was unavailable."

        errors = self.validate()

        self.assertTrue(any(".severity is not allowed for needs_validation" in error for error in errors), errors)

    def test_rejected_candidate_requires_reason_but_does_not_receive_severity(self):
        finding = self.findings["findings"][0]
        finding["state"] = "rejected"
        finding["rejection_reason"] = "The framework binds the value as a query parameter."
        self.findings["assessment"] = "no_confirmed_findings"
        for key in ("preconditions", "path_summary", "impact", "severity", "verification"):
            finding.pop(key)

        self.assertEqual(self.validate(), [])

    def test_complete_audit_requires_every_declared_unit_to_be_examined(self):
        self.coverage["required_unit_ids"].append("deployment-config")

        errors = self.validate()

        self.assertTrue(any("required coverage unit is missing: deployment-config" in error for error in errors), errors)

        self.coverage["required_unit_ids"] = ["tenant-read"]
        unit = self.coverage["units"][0]
        unit["status"] = "unsupported"
        errors = self.validate()
        self.assertTrue(any("coverage.units[0].status must be one of" in error for error in errors), errors)

        unit["status"] = "blocked"
        unit["gap"] = "The deployment snapshot is unavailable."
        errors = self.validate()
        self.assertTrue(any("unexamined required coverage unit: tenant-read" in error for error in errors), errors)

    def test_every_finding_must_be_accounted_for_by_a_coverage_unit(self):
        self.coverage["units"][0]["finding_ids"] = []

        errors = self.validate()

        self.assertTrue(any("finding is not linked to a coverage unit: SEC-001" in error for error in errors), errors)

    def test_source_and_evidence_references_cannot_escape_their_roots(self):
        self.findings["findings"][0]["source"]["path"] = "../outside.py"
        self.findings["findings"][0]["evidence"] = ["../outside.md"]

        errors = self.validate()

        self.assertTrue(any("safe root-relative path" in error for error in errors), errors)

        self.findings["findings"][0]["source"]["path"] = "missing.py"
        self.findings["findings"][0]["evidence"] = ["missing.md"]
        errors = self.validate()
        self.assertTrue(any("is unavailable" in error for error in errors), errors)

    def test_source_and_evidence_references_reject_symlinks(self):
        source_link = self.source_root / "linked.py"
        evidence_link = self.evidence_root / "linked.md"
        try:
            source_link.symlink_to("service.py")
            evidence_link.symlink_to("discovery.md")
        except (OSError, NotImplementedError) as error:
            self.skipTest(f"file symlinks unavailable: {error}")

        self.findings["findings"][0]["source"]["path"] = "linked.py"
        errors = self.validate()
        self.assertTrue(any("source.path must not follow a symlink or junction" in error for error in errors), errors)

        self.findings["findings"][0]["source"]["path"] = "service.py"
        self.findings["findings"][0]["evidence"] = ["linked.md"]
        errors = self.validate()
        self.assertTrue(any("evidence[0] must not follow a symlink or junction" in error for error in errors), errors)

    def test_completed_execution_can_have_incomplete_audit_and_unresolved_assessment(self):
        self.findings["audit_status"] = "incomplete"
        self.findings["assessment"] = "findings_present"
        self.coverage["units"][0]["status"] = "blocked"
        self.coverage["units"][0]["gap"] = "Required deployment evidence is unavailable."

        self.assertEqual(self.validate(), [])

        self.run_metadata["status"] = "confirmed"
        errors = self.validate()
        self.assertTrue(any("run metadata.status" in error for error in errors), errors)

    def test_validator_checks_source_paths_without_executing_target_code(self):
        marker = self.root / "target-was-executed.txt"
        payload = self.source_root / "service.py"
        payload.write_text(
            f"from pathlib import Path\nPath({str(marker)!r}).write_text('executed')\n",
            encoding="utf-8",
        )

        self.assertEqual(self.validate(run_metadata=False), [])
        self.assertFalse(marker.exists())

    def test_invalid_json_has_actionable_error(self):
        findings_path = self.control_root / "findings.json"
        findings_path.write_text("{not json", encoding="utf-8")
        coverage_path = self.control_root / "coverage-ledger.json"
        coverage_path.write_text(json.dumps(self.coverage), encoding="utf-8")

        errors = validator.validate_bundle(
            findings_path, coverage_path, self.source_root, self.evidence_root
        )

        self.assertTrue(any("cannot read findings as JSON" in error for error in errors), errors)

        findings_path.write_text('{"schema_version": 1, "schema_version": 1}', encoding="utf-8")
        errors = validator.validate_bundle(
            findings_path, coverage_path, self.source_root, self.evidence_root
        )
        self.assertTrue(any("duplicate JSON object key: schema_version" in error for error in errors), errors)

    def test_json_size_limit_applies_to_findings_coverage_and_run_metadata(self):
        self.validate()
        findings_path = self.control_root / "findings.json"
        coverage_path = self.control_root / "coverage-ledger.json"
        run_path = self.control_root / "run.json"
        paths = (
            ("findings", findings_path),
            ("coverage ledger", coverage_path),
            ("run metadata", run_path),
        )

        for label, path in paths:
            original = path.read_bytes()
            path.write_bytes(b" " * (validator.MAX_DOCUMENT_BYTES + 1))
            errors = validator.validate_bundle(
                findings_path,
                coverage_path,
                self.source_root,
                self.evidence_root,
                run_path,
            )
            self.assertTrue(any(f"{label} JSON exceeds the 8 MiB limit" in error for error in errors), errors)
            path.write_bytes(original)

    def test_excessive_json_nesting_is_actionable_and_cli_returns_nonzero(self):
        self.validate()
        findings_path = self.control_root / "findings.json"
        coverage_path = self.control_root / "coverage-ledger.json"
        run_path = self.control_root / "run.json"
        paths = (
            ("findings", findings_path),
            ("coverage ledger", coverage_path),
            ("run metadata", run_path),
        )
        depth = validator.MAX_JSON_NESTING + 1
        nested_json = b'{"nested":' + b"[" * depth + b"0" + b"]" * depth + b"}"

        for label, path in paths:
            original = path.read_bytes()
            path.write_bytes(nested_json)
            errors = validator.validate_bundle(
                findings_path,
                coverage_path,
                self.source_root,
                self.evidence_root,
                run_path,
            )
            self.assertTrue(any(f"{label} JSON nesting exceeds the 128-level limit" in error for error in errors), errors)
            path.write_bytes(original)

        findings_path.write_bytes(nested_json)
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            status = validator.main(
                [
                    "--findings", str(findings_path),
                    "--coverage", str(coverage_path),
                    "--source-root", str(self.source_root),
                    "--evidence-root", str(self.evidence_root),
                    "--run-metadata", str(run_path),
                ]
            )
        self.assertEqual(status, 1)
        self.assertIn("findings JSON nesting exceeds the 128-level limit", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_json_decoder_recursion_error_is_concise(self):
        self.validate()
        with patch.object(validator.json, "loads", side_effect=RecursionError):
            errors = validator.validate_bundle(
                self.control_root / "findings.json",
                self.control_root / "coverage-ledger.json",
                self.source_root,
                self.evidence_root,
                self.control_root / "run.json",
            )

        self.assertTrue(any("findings JSON nesting exceeds the supported parser depth" in error for error in errors), errors)

    def test_diagnostic_collection_is_bounded_and_reports_truncation(self):
        self.findings["findings"] = [None] * (validator.MAX_DIAGNOSTICS * 2)
        self.findings["assessment"] = "no_confirmed_findings"

        errors = self.validate()

        self.assertEqual(len(errors), validator.MAX_DIAGNOSTICS + 1)
        self.assertTrue(errors[-1].startswith("Further validation errors omitted"), errors[-1])
        self.assertTrue(all(len(error) <= validator.MAX_DIAGNOSTIC_LENGTH for error in errors), errors)

    def test_windows_without_junction_detection_fails_closed(self):
        self.validate()
        with patch.object(validator.sys, "platform", "win32"), patch.object(
            validator.Path, "is_junction", None, create=True
        ):
            errors = validator.validate_bundle(
                self.control_root / "findings.json",
                self.control_root / "coverage-ledger.json",
                self.source_root,
                self.evidence_root,
                self.control_root / "run.json",
            )

        self.assertEqual(
            errors,
            ["Windows path validation requires Python 3.12+ for reliable junction detection"],
        )

    def test_schema_version_must_be_an_integer_not_a_boolean(self):
        self.findings["schema_version"] = True

        errors = self.validate()

        self.assertTrue(any("findings.schema_version must be 1" in error for error in errors), errors)

    def test_unhashable_enum_values_are_reported_without_crashing(self):
        finding = self.findings["findings"][0]
        finding["severity"]["level"] = ["high"]
        errors = self.validate()
        self.assertTrue(any("severity.level must be one of" in error for error in errors), errors)

        finding["severity"]["level"] = "high"
        finding["verification"]["method"] = {"name": "fresh_context"}
        errors = self.validate()
        self.assertTrue(any("verification.method must be one of" in error for error in errors), errors)

        finding["verification"]["method"] = "fresh_context"
        self.run_metadata["status"] = []
        errors = self.validate()
        self.assertTrue(any("run metadata.status must be one of" in error for error in errors), errors)

    def test_run_metadata_must_follow_the_runtime_workspace_contract(self):
        self.run_metadata.pop("run_id")
        errors = self.validate()
        self.assertTrue(any("run metadata.run_id must be a non-empty string" in error for error in errors), errors)

        self.run_metadata["run_id"] = "../outside"
        self.run_metadata["created_at"] = "not-a-timestamp"
        self.run_metadata["scope"] = "tenant record read endpoint"
        errors = self.validate()
        self.assertTrue(any("run metadata.run_id must use portable" in error for error in errors), errors)
        self.assertTrue(any("created_at must be an ISO 8601 timestamp" in error for error in errors), errors)
        self.assertTrue(any("run metadata.scope must be an object" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
