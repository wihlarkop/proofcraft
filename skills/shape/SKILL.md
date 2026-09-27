---
name: shape
description: >-
  Shape software work into clear product behavior and decisions. Use when a feature/request is
  ambiguous, has unresolved human decisions, needs a behavioral specification, or is too uncertain
  for implementation planning. Supports normal shaping, spec mode, and wayfinding for large fog-
  of-war work. Inspect the repository for facts instead of asking the user to relay them.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Shape

Convert ambiguous intent into behavior and decisions clear enough for planning.

## Modes

- **shape** — normal product/behavior clarification.
- **spec** — user already knows the desired behavior; produce or update the behavioral contract directly.
- **wayfind** — large uncertain work where bounded research/prototypes are needed before a stable plan exists.

## Workflow

1. Run a focused reality check and read relevant durable product/architecture decisions.
2. Separate repository facts from human decisions. Discover facts yourself when tools/environment expose them.
3. Identify the current decision frontier: questions whose answers actually change behavior, scope, compatibility, or architecture.
4. Resolve behavior and product constraints. Do not interrogate the user about naming/file-placement decisions the repository can decide locally.
5. Detect material domain/architecture concerns and report them to the active workflow rather than selecting providers.
6. Produce/update a specification when the work is substantial enough to benefit from a durable behavioral contract.

## Specification boundary

The spec states WHAT must be true: behavior, invariants, lifecycle/failure semantics, compatibility expectations, acceptance criteria, and explicit non-goals. Implementation details belong in the plan.

## Stop

Stop when the work is clear enough to plan, or when one or more genuine human decisions remain and guessing would create meaningful product/architecture risk.
## Reference Guide

Load only the references needed for the current task:

- [spec mode](references/spec-mode.md)
- [wayfinding](references/wayfinding.md)
- [principles](references/_shared/constitution/principles.md)
- [decision lock](references/_shared/constitution/decision-lock.md)
- [reality check](references/_shared/orchestration/reality-check.md)
- [depth](references/_shared/orchestration/depth.md)
- [concerns](references/_shared/orchestration/concerns.md)
- [artifact model](references/_shared/artifacts/artifact-model.md)
- [spec](references/_shared/artifacts/spec.md)
- [provider neutrality](references/_shared/engineering/provider-neutrality.md)
