---
name: plan
description: >-
  Create an adaptive implementation plan from a clear request or specification. Use when a change
  has enough implementation complexity to benefit from an execution contract. Inspect project
  reality, classify depth and concerns, compose only relevant specialist capabilities, and produce
  enough detail for a fresh agent to implement without re-deciding architecture. Avoid line-by-
  line pseudo-code, invented product policy, and mandatory TDD.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.1"
---


# Plan

Create the smallest implementation contract that removes meaningful ambiguity.

## Workflow

1. Start from the current project workspace and its durable product/spec/ADR/context artifacts. Do not search harness-wide/global/personal memory unless the user explicitly asks to reuse prior context or the workspace itself points to it. Detect whether the workspace is a Git repository before running Git commands; non-Git is a normal project state.
2. Reality-check accepted decisions and direct contradictions. If a stale summary/pointer directly conflicts with a clearly authoritative accepted artifact, minimally reconcile the stale summary when safe; otherwise surface the contradiction as a blocker rather than silently choosing.
3. Classify work depth: direct, bounded, substantial, or high-assurance. A direct task may not need a formal plan.
4. Identify primary and supporting concerns before selecting specialists.
5. Compose only domain capabilities that materially affect the plan. Domain skills report additional concerns; this skill remains the orchestration owner.
6. Preserve existing architecture and provider choices unless the requested change explicitly revisits them.
7. Separate product decisions from implementation decisions. Do not invent user-visible behavior, supported platforms, validation policy, ordering semantics, lifecycle promises, or other product policy merely to make the plan feel complete. Ask/route back to shape when such a decision blocks an executable plan. Reversible implementation details may be selected when they stay within accepted product and architecture constraints.
8. Break substantial work into coherent behavior slices with clear interfaces/dependencies rather than test-first microsteps.
9. Define failure behavior and verification proportional to risk.

## Plan depth

For bounded work, prefer Goal / Current behavior / Change / Files-or-modules / Edge cases / Verification.

For substantial work, add architecture/contracts, state/lifecycle, compatibility or migration, task dependencies, acceptance, and rollout where relevant.

Use the implementation contract pattern from the shared plan reference.

## Testing

Verification is required. TDD is optional and should be selected only when the user asks for it, the project requires it, or it clearly improves this task.

## Stop

Apply the fresh-agent test: with the project and plan, a capable agent can implement without reopening settled architecture or inventing unresolved product behavior. If a material human decision still blocks execution, stop at that decision instead of guessing. Stop before the plan becomes source code written in prose.
