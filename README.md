# Proofcraft

**Low-ceremony, evidence-driven Agent Skills for shaping, building, verifying, and shipping software across coding agents.**

Proofcraft is a cross-harness software-engineering skill suite. It favors implementation over ceremony, evidence over assumptions, adaptive depth over rigid methodology, and capabilities over vendors.

The suite follows the portable Agent Skills shape (`SKILL.md` plus on-demand references/assets/scripts). Provider- and harness-specific capabilities are optional enhancements rather than architectural defaults.

## Status

Proofcraft is in early development (`v0.x`) and is being dogfooded before the public workflow contract is stabilized at `v1.0.0`.

The current checkpoint implements all **10 core orchestration skills** plus **7 domain skills**. The remaining domain layer is tracked in `suite.yaml`.

## Core workflow

The human-facing workflow stays intentionally small:

```text
setup -> shape/architect -> plan -> implement/debug -> accept/review -> finish
```

`continue` reconstructs repository reality and resumes from the correct stage. This is not a mandatory waterfall: direct work can skip stages, while high-risk work gets deeper evidence.

### Core skills

| Skill | Purpose |
| --- | --- |
| `setup` | Initialize or reconcile thin repository context and `AGENTS.md` guidance. |
| `shape` | Resolve product ambiguity, decisions, specs, and wayfinding when needed. |
| `architect` | Make consequential architecture decisions and record tradeoffs. |
| `plan` | Produce implementation contracts with depth proportional to the work. |
| `implement` | Execute coherent feature slices implementation-first. |
| `accept` | Prove observable behavior with risk-appropriate evidence. |
| `debug` | Reproduce, isolate root cause, fix, and protect against regression. |
| `review` | Review the intended change with evidence-backed findings. |
| `finish` | Verify, reconcile, check diff hygiene, and produce closure/handoff evidence. |
| `continue` | Reconstruct current truth and resume the first eligible work. |

### Implemented domain skills

| Skill | Purpose |
| --- | --- |
| `ui-engineering` | Surface-aware UI engineering for web, desktop, mobile UI, and hybrid/WebView experiences. |
| `mobile-engineering` | Mobile lifecycle/background behavior, local-first/offline sync, device concerns, and native/hybrid boundaries. |
| `database-engineering` | Application data modeling, constraints, transactions, query shapes, and indexes. |
| `migration-engineering` | Safe current-to-target transitions, compatibility windows, reconciliation, cutover, and deprecation. |
| `api-design` | Consumer-facing HTTP/RPC/GraphQL/event/webhook contracts, failures, idempotency, and evolution. |
| `integration-engineering` | External-system boundaries, mapping, rate limits/retries, webhooks/polling, and reconciliation. |
| `async-work` | Background jobs, queues/events, ownership, acknowledgement, retries, ordering, cancellation, replay, and backpressure. |

Domain skills are normally composed by a core workflow from detected concerns; users do not need to invoke every specialist manually.

## Principles

- Inspect before asking.
- Existing architecture before invention.
- Problem before pattern.
- Capability first, provider last.
- Implementation-first; verification mandatory.
- TDD is supported but never automatically required.
- Acceptance validates product behavior, not only tests.
- Durable knowledge has one owner.
- Preserve unrelated working-tree changes.
- Stop when evidence is sufficient.

## Install

Install from GitHub with an Agent Skills-compatible installer:

```bash
npx skills add wihlarkop/proofcraft
```

Update installed skills through the installer rather than mutating a project automatically:

```bash
npx skills update
```

Updating Proofcraft never authorizes rewriting a repository. Project-context migrations remain an explicit `/setup` concern.

## Repository layout

```text
src/shared/   canonical reusable methodology and artifact guidance
src/skills/   canonical skill sources edited by maintainers
skills/       generated, self-contained distributable Agent Skills
scripts/      stdlib-only build and validation tooling
evals/        suite-level routing, ceremony, and assurance cases
docs/         architecture, provider integration, and provenance notes
```

`skills/` is generated. Edit `src/`, then rebuild.

## Development

```bash
python scripts/build.py
python scripts/validate.py
python scripts/check_generated.py
```

The source manifests use JSON syntax stored in `.yaml` files. JSON is a YAML subset, which keeps the authoring toolchain Python-stdlib-only.

## Design boundaries

Proofcraft separates four layers:

1. **Core workflows** own orchestration.
2. **Domain skills** contribute specialist engineering reasoning.
3. **Shared references** hold focused techniques and reusable methodology.
4. **Optional providers** enhance a capability only when they match the project already in front of the agent.

A provider being installed is never evidence that the project should adopt it.

See `docs/architecture.md`, `docs/provider-integration.md`, and `docs/influences.md` for the current design contract and provenance notes.

## License

MIT © 2026 Wihlarko Prasdegdho. See `LICENSE`.
