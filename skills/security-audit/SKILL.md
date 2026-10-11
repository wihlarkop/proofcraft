---
name: security-audit
description: >-
  Conduct an explicitly requested, scoped or full-repository security audit. Use for
  source-first vulnerability discovery with coverage accounting, validated findings, and
  independent verification. Ordinary PR/diff review remains with review; threat modeling
  and secure design remain with the active core workflow and security-engineering.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---

# Security Audit

Own the lifecycle of an explicitly requested security audit. Compose security-engineering for threat modeling and trust-boundary expertise. Keep this workflow as the sole core owner: do not invoke review, accept, debug, implement, or another core workflow to perform audit phases. Report remediation guidance; remediation is a separate authorized task.

## Routing

- “Audit this repository for vulnerabilities” → security-audit, full repository scope.
- “Audit authentication and tenant isolation in this module” → security-audit, explicit component scope.
- “Review the authorization changes in this PR” → review, with relevant security concerns.
- “Threat model this feature” → the active core workflow with security-engineering.
- “Fix this confirmed vulnerability” → debug or implement, as appropriate.

Security-sensitive subject matter alone does not trigger a full audit.

## Six-phase lifecycle

1. **Reconnaissance:** establish authorized scope and source identity; map relevant architecture, entry points, principals and privilege boundaries, sensitive assets and operations, attack surfaces, available and missing evidence, and an auditable coverage plan.
2. **Coverage-led hunting:** inspect the planned implementation paths and select applicable attack classes such as authentication/authorization, tenant isolation, injection/deserialization, filesystem/process, SSRF/network, secrets/privilege, supply chain, or AI/tool trust. This is not a mandatory checklist. Trace attacker-controlled input or authority to a sensitive sink or action. Record examined and unexamined surfaces.
3. **Candidate validation:** trace reachability and surrounding controls, account for framework/runtime protections and deployment assumptions, and seek evidence that could disprove each material hypothesis.
4. **Structured findings:** maintain versioned findings.json and coverage-ledger.json using references/audit-contract.md. Preserve rejected candidates with their reason; unresolved hypotheses have no numeric severity. A confirmed finding requires a recorded independent-verifier conclusion of `supports`; a `refutes` conclusion belongs on a rejected candidate, while `inconclusive` or unavailable verification remains needs_validation without severity.
5. **Independent verification:** attempt to falsify every candidate proposed as confirmed using a genuinely separate reviewer or fresh context. Record the conclusion as `supports`, `refutes`, or `inconclusive`, separately from the human-readable result explanation. A structured conclusion is an attestation, not proof that the reviewer was genuinely independent or that the vulnerability exists. If that capability is unavailable, keep it needs_validation, state the limitation, and do not invent verifier identity or outcome.
6. **Reporting:** produce report.md from the scope, coverage, findings, and evidence. State confirmed findings, validation needs, useful rejected candidates, gaps, bounded remediation guidance, verification limits, and overall audit status. Zero confirmed findings does not mean “secure.”

An audit can finish its available source analysis with unresolved findings. If required scope or verification cannot be completed, report the audit as incomplete or blocked rather than claiming full verification.

## Execution boundary

M1 is source-first and non-executing against untrusted target code. Do not run target build/install scripts, dependency hooks, tests, application commands, binaries, production requests, or exploit payloads. Read-only permission is not execution permission. Run only the bundled trusted findings validator against audit JSON and file references. See references/source-only-safety.md.

## Evidence

Use the project’s established artifact convention. For retained trusted control-side evidence, follow references/_shared/artifacts/runtime-workspace.md and use .proofcraft/runs/security-audit/<run-id>/ only when safe and appropriate. For an untrusted audited repository, prefer an external control-side output location unless a safe project-local destination was already established. Do not create an unignored .proofcraft/ directory just to store audit output. .proofcraft/ is not a sandbox.

Keep runtime lifecycle (run.json status) separate from audit status, assessment, and individual finding state. Retain only necessary evidence; avoid secrets and sensitive production payloads. Never stage runtime evidence automatically or delete historical runs.

## Stop

Stop when the requested scope, coverage, evidence, candidate dispositions, independent-verification limits, and audit status are explicit. Do not claim coverage beyond what the ledger and inspected source support.
## Reference Guide

Load only the references needed for the current task:

- [audit contract](references/audit-contract.md)
- [source only safety](references/source-only-safety.md)
- [principles](references/_shared/constitution/principles.md)
- [decision lock](references/_shared/constitution/decision-lock.md)
- [reality check](references/_shared/orchestration/reality-check.md)
- [concerns](references/_shared/orchestration/concerns.md)
- [diff discipline](references/_shared/engineering/diff-discipline.md)
- [runtime workspace](references/_shared/artifacts/runtime-workspace.md)
- [evidence](references/_shared/verification/evidence.md)
- [risk depth](references/_shared/verification/risk-depth.md)
