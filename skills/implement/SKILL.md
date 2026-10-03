---
name: implement
description: >-
  Implement a clear bounded task or approved plan using coherent feature slices. Use after
  behavior and necessary architecture decisions are clear. Inspect and protect the working tree,
  preserve unrelated changes and open decisions, compose material domain specialists, implement
  product behavior first, then collect targeted automated/integration evidence. TDD is supported
  when explicitly selected but is not the default workflow.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.4"
---


# Implement

Execute a clear change without re-deciding product or architecture unnecessarily.

## Entry

Use when a plan is ready or a bounded task is sufficiently clear to implement directly. If substantial behavioral/architecture ambiguity remains, route back to shape/architect/plan rather than guessing.

## Workflow

1. Reality-check project-local code, accepted artifacts, available capabilities, and working-tree/source-control state when applicable. Preserve unrelated changes.
2. For substantial work, verify prerequisites with a lightweight gate.
3. Classify the material implementation concerns, then load each relevant domain skill contract before making that part of the change. Typical examples include UI, mobile lifecycle/offline behavior, and database persistence. Do not treat broad skill-tree discovery as composition, and do not load incidental specialists.
4. Preserve settled decisions and preserve explicitly open decisions. Reversible implementation mechanisms may be chosen when needed to realize accepted behavior, but do not promote them into new product policy or architecture truth.
5. Implement one coherent behavior slice at a time. Prefer existing supported project patterns and dependencies. When a selected language/framework/library/tool has version-sensitive or unestablished usage, follow the current-technology-usage contract and consult current primary guidance only for the capability being used. When a new dependency is justified, follow the dependency-selection contract and record the reason proportionally.
6. Keep business/domain intent separate from vendor/framework plumbing where the project architecture already does so.
7. Select verification against the actual surface where the changed behavior can fail, using `references/_shared/verification/verification-surfaces.md` when browser/UI, HTTP/GraphQL, RPC/gRPC, async/event, persistence, CLI, or device/runtime behavior is material. Reuse the project's existing supported runner/tooling. Before setup or verification can mutate external state, load `references/_shared/engineering/test-environment-isolation.md` and confirm isolated setup, actual runtime, and test targets; otherwise block the write-capable run. Run the cheapest useful static/build evidence after meaningful slices, then add targeted regression/integration coverage appropriate to risk. Verification is required, but unit tests and coverage targets are not mandatory by default. Add focused unit tests when they are the cheapest strong evidence for meaningful logic/invariants or when the project/user requires them. Do not force red-green-refactor unless TDD was explicitly selected.
8. Exercise the strongest relevant runnable surface that is actually available. If a required device/toolchain is unavailable, record that verification as blocked rather than substituting an irrelevant platform or claiming equivalent evidence.
9. Avoid unrelated cleanup and refactors unless required for correctness or explicitly accepted. Expected no-match cleanup searches are normal evidence; run them so a no-match does not masquerade as a failed implementation step.
10. Keep this workflow as the core owner. Do not preload or execute accept, review, or finish merely to make implementation feel complete; hand off when their workflow is actually requested or becomes the next phase.

## Stop

Stop implementation when the requested behavior is runnable to the strongest available degree and ready for acceptance/verification, with any environment-blocked evidence stated explicitly. Do not turn implementation into an endless polish/review loop.
## Reference Guide

Load only the references needed for the current task:

- [principles](references/_shared/constitution/principles.md)
- [decision lock](references/_shared/constitution/decision-lock.md)
- [reality check](references/_shared/orchestration/reality-check.md)
- [concerns](references/_shared/orchestration/concerns.md)
- [gate](references/_shared/orchestration/gate.md)
- [diff discipline](references/_shared/engineering/diff-discipline.md)
- [dependency selection](references/_shared/engineering/dependency-selection.md)
- [technology usage](references/_shared/engineering/technology-usage.md)
- [risk depth](references/_shared/verification/risk-depth.md)
- [verification surfaces](references/_shared/verification/verification-surfaces.md)
- [regression scope](references/_shared/verification/regression-scope.md)
- [test environment isolation](references/_shared/engineering/test-environment-isolation.md)
