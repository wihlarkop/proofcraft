---
name: privacy-engineering
description: >-
  Translate privacy requirements into engineering behavior across data purpose, minimization,
  access, retention, deletion, consent, residency, derived data, telemetry, and AI traces. Use
  when a feature collects or processes personal/sensitive data or must prove lifecycle behavior.
  Keep legal interpretation outside this skill; privacy owns what data should exist and for how
  long, while security owns protection mechanisms.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Privacy Engineering

Engineer the full data lifecycle from purpose through deletion.

## Workflow

1. State the declared purpose for each material data category and reject speculative collection that has no concrete use.
2. Classify data sensitivity and map collection, processing, storage, access, sharing, derived copies, logs/telemetry, backups, and deletion.
3. Define minimization: collect only what the product requirement actually needs.
4. Define retention trigger and duration from accepted product/legal policy; do not invent jurisdiction-specific legal requirements.
5. Define consent/revocation behavior where applicable, including how system behavior changes after revocation.
6. Define deletion propagation across primary stores, replicas, caches, exports, traces, and derived datasets as required by the policy.
7. Convert privacy requirements into observable acceptance criteria and verify deletion/retention behavior rather than trusting documentation alone.
8. Route encryption/authz/secrets implementation to security-engineering and storage mechanics to database/platform specialists.

## Stop

Stop when relevant personal/sensitive data has a clear purpose, lifecycle, retention/deletion behavior, and verifiable privacy acceptance criteria.
## Reference Guide

Load only the references needed for the current task:

- [data lifecycle](references/data-lifecycle.md)
- [deletion verification](references/deletion-verification.md)
- [telemetry ai traces](references/telemetry-ai-traces.md)
- [principles](references/_shared/constitution/principles.md)
- [decision lock](references/_shared/constitution/decision-lock.md)
- [concerns](references/_shared/orchestration/concerns.md)
- [authority](references/_shared/state/authority.md)
- [cache](references/_shared/state/cache.md)
- [evidence](references/_shared/verification/evidence.md)
- [risk depth](references/_shared/verification/risk-depth.md)
