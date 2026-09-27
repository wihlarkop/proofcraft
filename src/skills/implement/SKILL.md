---
name: implement
description: >-
  Implement a clear bounded task or approved plan using coherent feature slices. Use after
  behavior and necessary architecture decisions are clear. Inspect and protect the working tree,
  preserve unrelated changes, implement product behavior first, then collect targeted
  automated/integration evidence. TDD is supported when explicitly selected but is not the default
  workflow.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Implement

Execute a clear change without re-deciding product or architecture unnecessarily.

## Entry

Use when a plan is ready or a bounded task is sufficiently clear to implement directly. If substantial behavioral/architecture ambiguity remains, route back to shape/architect/plan rather than guessing.

## Workflow

1. Reality-check the branch, intended base, current code, and working tree. Preserve unrelated changes.
2. For substantial work, verify prerequisites with a lightweight gate.
3. Implement one coherent behavior slice at a time. Prefer existing patterns and dependencies.
4. Keep business/domain intent separate from vendor/framework plumbing where the project architecture already does so.
5. Run the cheapest useful static/build evidence after meaningful slices.
6. Add targeted regression/integration coverage appropriate to the risk. Do not force red-green-refactor unless TDD was explicitly selected.
7. Avoid unrelated cleanup and refactors unless required for correctness or explicitly accepted.

## Stop

Stop implementation when the requested behavior is runnable and ready for acceptance/verification. Do not turn implementation into an endless polish/review loop.
