# Repository Architecture

## Authoring and distribution

Canonical methodology lives under `src/`. Canonical skill instructions use `src/skills/<name>/SOURCE.md`, deliberately avoiding the reserved discoverable filename `SKILL.md`.

Build tooling emits self-contained skills under `skills/<name>/SKILL.md`. This gives the repository exactly one discoverable Agent Skill path per skill name while still keeping authoring sources separate from generated distribution.

Shared references are copied only into skills that declare them. This keeps authoring DRY while preserving portable distribution and progressive disclosure.

## Composition hierarchy

1. A core workflow owns orchestration.
2. The workflow resolves relevant domain concerns.
3. Domain skills use focused shared references.
4. Optional provider integrations enhance a capability only when they match the current project.

Domain skills do not take over orchestration and do not recursively invoke each other. They may report an additional concern to the active workflow owner.

Utility skills are explicit, bounded transformations outside the engineering lifecycle. They consume canonical artifacts without becoming their owner. For example, `artifact-export` may emit an OpenSpec representation of settled Proofcraft knowledge while leaving Proofcraft project truth unchanged.

## Runtime philosophy

The suite classifies work by work class, depth, and concerns. Depth is adaptive: direct, bounded, substantial, or high-assurance. Verification depth follows risk rather than a mandatory process.

## Artifact ownership

- `AGENTS.md`, project orientation: setup
- Product truth/specification: shape
- Architecture decisions: architect/ADR helper
- Implementation plan: plan
- Code: implement for new behavior; improve for behavior-preserving quality changes; debug for evidenced repairs
- Acceptance evidence: accept
- Closure/reconciliation/handoff: finish
- External collaboration representations: artifact-export (derived by default; never the canonical owner unless the project explicitly adopts the target format)

Durable facts should have one canonical owner.
