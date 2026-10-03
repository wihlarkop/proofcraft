---
name: improve
description: >-
  Improve an existing implementation without silently changing product behavior. Use for
  refactoring, cleanup, idiomatic modernization, maintainability, simplification, bounded
  code-quality work, or a repository-wide improvement audit on software that already substantially
  works. Inspect real code and selected technology versions, compose only material domain concerns,
  prefer concrete high-value changes over pattern shopping, verify preserved behavior, and leave
  already-good code alone.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.2"
---


# Improve

Make existing code materially better without manufacturing work or changing its contract by accident.

## Entry

Use when the implementation already works or mostly works and the requested outcome is refactoring, cleanup, simplification, idiomatic modernization, maintainability, another bounded quality improvement, or discovery of worthwhile improvement opportunities across an existing codebase. Default preservation boundary: externally observable product behavior, accepted architecture, data contracts, and explicitly open decisions stay unchanged unless the user explicitly requests otherwise.

## Workflow

1. Reality-check project-local code, accepted artifacts, selected versions/configuration, available evidence, and working-tree/source-control state. Preserve unrelated changes.
2. Establish the target and preservation boundary. Understand what must stay behaviorally identical and what kind of improvement the user actually wants.
   - For a bounded target, inspect that implementation and its direct owners.
   - For a repository-wide request to **scan**, **audit**, or **find what should be improved**, start in read-only discovery mode. Inspect project orientation, manifests/configuration, major ownership boundaries, verification surfaces, and representative or high-risk implementation paths. Follow evidence to deeper hotspots rather than mechanically reading every file. The output of a discovery-only request is a prioritized improvement frontier, not automatic churn.
   - If the user already authorized codebase-wide improvement rather than discovery only, use that frontier to select a bounded first change; do not turn broad permission into an unbounded rewrite.
3. Classify material concerns and load only the relevant domain skill contracts. Improve remains the core workflow owner; specialists contribute evidence rather than taking over orchestration.
4. Inspect the actual implementation before proposing a pattern. Follow the current-technology-usage contract for the selected language, runtime, framework, library, database, build tool, and developer tooling. Consult current primary guidance only where usage is version-sensitive, unfamiliar, or materially changed.
5. Build a bounded improvement frontier:
   - **MUST** — unsupported/deprecated usage, accepted-architecture violations, correctness-adjacent hazards, or severe maintainability problems directly in scope.
   - **WORTHWHILE** — concrete simplification, clearer ownership, duplicate-rule removal, or idiomatic improvements with material value.
   - **OPTIONAL** — subjective style, speculative abstractions, or tiny cleanup with weak payoff.
   - **OUT OF SCOPE** — product behavior changes, durable architecture redesign, unrelated subsystems, or performance rewrites without evidence.
6. Route rather than blur ownership when the primary problem changes. An actual failing behavior belongs to debug; a consequential architecture change belongs to architect; unresolved user-visible behavior belongs to shape. If performance/resource efficiency is the real target, compose performance-engineering and establish a relevant baseline before changing code.
7. Select only the MUST and worthwhile bounded changes that justify their churn. Prefer **delete -> consolidate -> use language/framework/native-tool mechanisms -> rehome responsibility into an existing owner -> only then introduce a new abstraction**. This is a preference order, not an absolute rule.
8. Before accepting a new abstraction, require an evidenced benefit that outweighs the concept added. Apply the net complexity check in `references/_shared/engineering/simplification.md` before and after the change; fewer lines or a replacement wrapper alone do not establish improvement. Do not add named architecture patterns or generic layers merely because a template recommends them.
9. Before setup or verification can mutate external state, load `references/_shared/engineering/test-environment-isolation.md` and confirm isolated setup, actual runtime, and test targets; otherwise block the write-capable run. Verify the preservation boundary and the changed concern with proportional evidence. Verification is required; unit tests, TDD, and coverage targets are not mandatory. Add a focused test only when it is the cheapest strong evidence for a meaningful invariant/regression or when required by the project/user.

If inspection shows the code is already clear, supported, idiomatic, and proportionate, say so and leave it unchanged.

## Outputs

For discovery-only audits, report the evidence-backed improvement frontier, why each item matters, and a bounded next target without editing code. For implemented improvements, report the bounded changes and relevant net complexity change, preserved contract, verification evidence, and any deferred item requiring another workflow decision.

## Stop

Before stopping, check whether in-scope wrappers, ownership splits, composition hops, or intermediate artifacts can still be removed. Stop when the target is materially improved and remaining changes have weak payoff or require another workflow decision; leave already-proportionate code alone.
