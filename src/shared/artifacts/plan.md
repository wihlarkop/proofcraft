# Implementation Plan Contract

Planning removes implementation ambiguity without writing the code in prose.

A useful implementation contract can include:

- Goal
- Delivers
- Touches
- Consumes / Produces
- Must preserve
- Failure behavior
- Verification
- Done when

For larger work add dependencies, architecture implications, state/lifecycle, migration/compatibility, rollout, and a task graph.

## Decision discipline

A plan inherits accepted product and architecture decisions; it does not manufacture missing product policy. User-visible behavior, supported platforms, validation rules, ordering semantics, lifecycle promises, and other durable product choices must come from accepted requirements or an explicit human decision.

The planner may choose reversible implementation details that stay within accepted constraints. If a missing human decision materially blocks execution, surface or route that decision back to shaping instead of hiding it as an “assumption.”

Fresh-agent test: a capable agent with the project and plan should be able to implement the work without re-deciding architecture or inventing unresolved product behavior. If the plan reads like source code, it is too detailed.
