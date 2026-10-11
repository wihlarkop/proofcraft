# Security Audit Evidence Contract

Version 1 uses two JSON documents and the optional Runtime Workspace run.json. Keep scope and source identity identical in the findings and coverage documents. These files are audit evidence, not durable project knowledge.

## findings.json

The top-level object contains:

- schema_version: integer 1;
- source_identity: non-empty revision or explicit snapshot identity;
- scope: concise, authorized scope description;
- audit_status: complete, incomplete, or blocked;
- assessment: findings_present, no_confirmed_findings, or not_determined;
- findings: array of candidate records.

Each candidate has a unique non-empty id, title, vulnerability_class, boundary, state, source, and non-empty evidence array. source has a source-root-relative path and positive line_start; optional line_end must be at least line_start. Evidence entries are evidence-root-relative file paths.

State-specific requirements:

- confirmed: non-empty preconditions, path_summary, impact, and bounded remediation guidance; severity object with level (critical, high, medium, or low) and rationale; and verification with status independently_verified, verifier, method (separate_reviewer or fresh_context), distinct non-empty discovery and verification context IDs, falsification attempt, conclusion, result explanation, and evidence references. conclusion is supports, refutes, or inconclusive; confirmed requires supports. Refuted candidates should be rejected with a reason and evidence; inconclusive or unavailable verification remains needs_validation without severity. The validator checks this recorded contract; it cannot prove that the human process was genuine or that a reported vulnerability exists.
- needs_validation: a specific hypothesis, non-empty unresolved_facts, and non-empty validation_steps. It must not contain a severity field.
- rejected: non-empty rejection_reason and supporting evidence. Rejected candidates do not receive severity.

The assessment must match the evidence: any confirmed finding means findings_present; zero confirmed findings with a complete audit means no_confirmed_findings; zero confirmed findings with an incomplete or blocked audit means not_determined. “No confirmed findings” is not a claim that the system is secure.

## coverage-ledger.json

The top-level object contains schema_version 1, the same source_identity and scope, non-empty required_unit_ids, and units.

Each unit has a unique non-empty id, boundary, and status: examined, partially_examined, blocked, or not_examined. It includes observations, source_paths, evidence references, finding_ids, and, when not fully examined, a gap. Examined units need observations and at least one source or evidence reference. Any unit that is not fully examined needs a concrete gap. Source and evidence paths are relative to their respective roots; referenced findings must exist, and every finding must be linked to a coverage unit.

Every required unit ID must appear in units. A complete audit requires every required unit to be examined. The ledger accounts only for the declared plan; it cannot prove the plan covers every risk in a repository.

## Lifecycle separation

When supplied with --run-metadata, run.json must include a portable run_id, an ISO 8601 created_at timestamp with timezone, workflow security-audit, scope.target (the same scope description as findings.scope), and lifecycle status running, completed, or incomplete. Optional source_revision, when present, must match findings.source_identity; incomplete_reason must be a non-empty string when supplied. It must not contain an audit verdict. A completed execution may contain an incomplete or blocked audit; the validator checks the two fields independently. Findings and coverage must also match each other on source_identity and scope.

## Validation command

Run the packaged standard-library validator from the generated skill directory:

    python validate_audit.py --findings <findings.json> --coverage <coverage-ledger.json> --source-root <audited-source-root> --evidence-root <evidence-root> [--run-metadata <run.json>]

The validator checks version, states, required fields, cross-document consistency, required coverage, lifecycle separation, and source/evidence references. References must be relative, use /, remain beneath their specified root, and resolve to regular non-linked files. Each JSON input is limited to 8 MiB and 128 nesting levels; at most 100 diagnostics (plus one truncation notice) are retained, and each diagnostic is limited to 512 characters. These limits bound local validation of audit evidence, not the size of the audited repository. On Windows, use Python 3.12 or newer so junctions can be detected; older Windows runtimes fail closed before path validation. It reads metadata and file paths only; it does not execute target code. A valid document is not proof that a finding is exploitable or that independent verification actually occurred.
