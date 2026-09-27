---
name: finish
description: >-
  Close software work with risk-appropriate verification, relevant review, diff hygiene, artifact
  reconciliation, readiness evidence, and a factual handoff. Use when implementation is considered
  complete, a PR/milestone should be ready, or release readiness must be assessed. Scale closure
  to the work: lightweight for small changes, deeper for migrations/security/production-risk work.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Finish

Close the work with enough evidence to make the completion claim credible, but no more ceremony than the risk requires.

## Workflow

1. Reality-check current branch/HEAD, working tree, intended change, and available CI/review evidence.
2. Reconstruct the work depth and material concern set; do not blindly reuse stale plan metadata.
3. Collect required verification/acceptance evidence and perform relevant review for the touched risk domains.
4. Check the final diff and protect unrelated changes.
5. Reconcile spec/plan/product/design/ADR/roadmap only where delivered truth changed durable truth.
6. For production/high-assurance changes, include the relevant migration, security, recovery, rollback, or readiness evidence. Do not run these modes for ordinary small changes.
7. Produce a factual evidence ledger/handoff when future continuation or PR review benefits from it.

## Release mode

When explicitly used for release readiness, verify artifact/version/compatibility/rollback and production-intended configuration appropriate to the project. A feature flag can stop future code paths but cannot reverse already-committed data or external side effects.

## Stop

Stop when required criteria are evidenced or explicitly marked blocked/gap, the intended diff is understood, durable artifacts are reconciled, and the next state is unambiguous.
