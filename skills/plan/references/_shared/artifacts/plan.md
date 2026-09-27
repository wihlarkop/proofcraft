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

Fresh-agent test: a capable agent with the repository and plan should be able to implement the work without re-deciding the architecture. If the plan reads like source code, it is too detailed.
