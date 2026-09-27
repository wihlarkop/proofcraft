---
name: architect
description: >-
  Design or review consequential software architecture decisions from concrete drivers,
  constraints, boundaries, runtime behavior, tradeoffs, and evolution. Use for storage authority,
  service/module boundaries, distributed behavior, cross-platform architecture, major
  dependencies, or other durable system decisions. Prefer existing architecture, use patterns only
  after the problem is clear, and produce an ADR when a decision is durable.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Architect

Make consequential system decisions without turning routine implementation into architecture ceremony.

## Trigger

Use when the task materially changes system boundaries, data authority, runtime/process topology, distributed semantics, platform shape, cross-platform architecture, or a hard-to-reverse dependency.

Do not trigger for routine helper extraction, local naming, styling, or an implementation pattern that is already established by the repository.

## Workflow

1. Reality-check the current architecture and accepted decisions.
2. Frame the decision: desired outcome, constraints, reversibility, affected systems, and evidence gaps.
3. Express material qualities as observable scenarios rather than vague adjectives.
4. Compare candidate boundaries/approaches against the same drivers.
5. Make data authority, runtime behavior, consistency, failure/recovery, and operational consequences explicit when relevant.
6. Select patterns only after the concrete problem is named; prefer existing project patterns.
7. Record a durable ADR when the decision is consequential and likely to matter beyond the current task.

## Outputs

Architecture brief, tradeoff decision, and optionally an ADR. Domain specialists may supply evidence, but this skill owns the architecture decision workflow.

## Stop

Stop when the decision, alternatives, consequences, evidence gaps, and downstream implementation/migration handoffs are explicit. Do not continue polishing an already sufficient architecture record.
## Reference Guide

Load only the references needed for the current task:

- [principles](references/_shared/constitution/principles.md)
- [decision lock](references/_shared/constitution/decision-lock.md)
- [reality check](references/_shared/orchestration/reality-check.md)
- [concerns](references/_shared/orchestration/concerns.md)
- [artifact model](references/_shared/artifacts/artifact-model.md)
- [boundaries](references/_shared/architecture/boundaries.md)
- [tradeoffs](references/_shared/architecture/tradeoffs.md)
- [pattern selection](references/_shared/architecture/pattern-selection.md)
- [provider neutrality](references/_shared/engineering/provider-neutrality.md)
- [evidence](references/_shared/verification/evidence.md)
