---
name: plan
description: >-
  Create an adaptive implementation plan from a clear request or specification. Use when a change
  has enough implementation complexity to benefit from an execution contract. Inspect repository
  reality, classify depth and concerns, compose only relevant specialist capabilities, and produce
  enough detail for a fresh agent to implement without re-deciding architecture. Avoid line-by-
  line pseudo-code and mandatory TDD.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Plan

Create the smallest implementation contract that removes meaningful ambiguity.

## Workflow

1. Reality-check the repository and relevant accepted decisions.
2. Classify work depth: direct, bounded, substantial, or high-assurance. A direct task may not need a formal plan.
3. Identify primary and supporting concerns before selecting specialists.
4. Compose only domain capabilities that materially affect the plan. Domain skills report additional concerns; this skill remains the orchestration owner.
5. Preserve existing architecture and provider choices unless the requested change explicitly revisits them.
6. Break substantial work into coherent behavior slices with clear interfaces/dependencies rather than test-first microsteps.
7. Define failure behavior and verification proportional to risk.

## Plan depth

For bounded work, prefer Goal / Current behavior / Change / Files-or-modules / Edge cases / Verification.

For substantial work, add architecture/contracts, state/lifecycle, compatibility or migration, task dependencies, acceptance, and rollout where relevant.

Use the implementation contract pattern from the shared plan reference.

## Testing

Verification is required. TDD is optional and should be selected only when the user asks for it, the repository requires it, or it clearly improves this task.

## Stop

Apply the fresh-agent test: with the repository and plan, a capable agent can implement without reopening settled architecture. Stop before the plan becomes source code written in prose.
## Reference Guide

Load only the references needed for the current task:

- [implementation contract](references/implementation-contract.md)
- [principles](references/_shared/constitution/principles.md)
- [decision lock](references/_shared/constitution/decision-lock.md)
- [bounded work](references/_shared/constitution/bounded-work.md)
- [reality check](references/_shared/orchestration/reality-check.md)
- [depth](references/_shared/orchestration/depth.md)
- [concerns](references/_shared/orchestration/concerns.md)
- [gate](references/_shared/orchestration/gate.md)
- [plan](references/_shared/artifacts/plan.md)
- [provider neutrality](references/_shared/engineering/provider-neutrality.md)
- [dependency selection](references/_shared/engineering/dependency-selection.md)
- [evidence](references/_shared/verification/evidence.md)
- [risk depth](references/_shared/verification/risk-depth.md)
