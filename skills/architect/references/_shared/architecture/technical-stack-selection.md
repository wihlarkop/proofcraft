# Technical Stack Selection

Use this when a greenfield project or an explicit architecture revisit must select a foundational language/runtime, application framework, client rendering model, database product, identity mechanism, or similarly durable stack component.

## Start from product forces, not technologies

Before naming candidates, derive the capabilities the stack must support from accepted product and architecture truth.

Consider only forces evidenced by the product's credible trajectory, including when relevant:

- interaction model and expected UI statefulness;
- authority for business rules and shared state;
- transactional and concurrency requirements;
- data shape and query behavior;
- client/platform targets;
- integration and background-work needs;
- security and identity boundaries;
- deployment and operational burden;
- expected evolution seams and additional clients;
- testability, observability, and failure diagnosis;
- maintenance horizon, ecosystem health, and upgrade path.

Do not optimize only for the first implementation slice when accepted product direction clearly contains near-term capabilities that would materially change the fit. Conversely, do not pay large complexity costs for speculative or explicitly deferred futures.

Use a weighted horizon:

1. **Now** — the accepted first coherent product/slice.
2. **Next** — accepted or strongly implied capabilities likely to arrive without changing the product's identity.
3. **Later** — deferred/speculative capabilities. Preserve an evolution path where cheap; do not optimize heavily for them.

## Compare stack shapes before brands

First identify credible architecture shapes, for example:

- integrated server-rendered application;
- server-rendered application with progressive enhancement;
- component frontend plus authoritative API/backend;
- full-stack JavaScript/TypeScript application;
- native/mobile client plus backend;
- another project-specific shape.

Then select concrete languages/frameworks only for the shapes that remain credible.

Do not assume:

- a SPA is inherently more modern or better;
- server rendering is inherently simpler for the whole product;
- one runtime is inherently preferable to two;
- a language/framework is appropriate because the agent or user already knows it;
- an installed provider/tool should influence selection;
- popularity alone is evidence of product fit.

## Candidate comparison

For a consequential choice, compare a small credible set against the same drivers. Prefer 2-4 serious candidates over a long technology catalog.

For each candidate, evaluate project-specific consequences:

- fit for the current interaction model;
- fit for the accepted near-term product trajectory;
- where domain/business rules live;
- state and validation duplication across boundaries;
- transactional/concurrency behavior;
- frontend/backend contract cost;
- development and build complexity;
- deployment/runtime topology;
- operational and debugging burden;
- security/auth implications;
- ecosystem/support lifecycle;
- portability and migration cost;
- what complexity is paid now versus deferred.

Explicitly separate:

- **durable architecture choices** — framework family, application/client boundary, database product, identity boundary, runtime topology, or similar decisions whose reversal would restructure the system;
- **upgradeable baselines** — supported runtime/framework versions when normal upgrades do not change architecture;
- **reversible tooling choices** — package managers, formatters, local developer utilities, and comparable conventions unless they create an external compatibility contract.

## Evidence

For claims that can change over time, prefer current primary sources such as official support policies, release documentation, database/runtime documentation, and security maintenance information.

Benchmarks are only relevant when the product has an evidenced performance requirement matching the benchmark. Do not choose a stack from synthetic benchmark leadership alone.

Developer familiarity may be listed as a delivery consideration when team capability is an explicit project constraint, but it must not substitute for use-case fit.

## Decision quality

A good stack decision explains not just why the selected stack works, but why its added boundaries and complexity are justified by the product.

Prefer the smallest stack whose complexity curve remains reasonable across **Now + Next**.

If the simplest first-slice stack is likely to create an avoidable architectural rewrite for already-accepted near-term capabilities, compare a slightly richer foundation now. If the richer stack only benefits speculative futures, keep the simpler stack.

Record material consequences and rejected alternatives in the ADR. Keep provider/deployment selections open when they are not required by the decision.
