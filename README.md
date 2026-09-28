# Proofcraft

**Low-ceremony, evidence-driven Agent Skills for shaping, building, verifying, and shipping software across coding agents.**

Proofcraft is a cross-harness software-engineering skill suite. It favors implementation over ceremony, evidence over assumptions, adaptive depth over rigid methodology, and capabilities over vendors.

The suite follows the portable Agent Skills shape (`SKILL.md` plus on-demand references/assets/scripts). Provider- and harness-specific capabilities are optional enhancements rather than architectural defaults.

## Status

Proofcraft is in early development (`v0.x`). The first public release is `v0.1.0`; the workflow contract will continue to evolve before `v1.0.0`.

Release `v0.1.0` implements the full planned v0.1 surface: **10 core orchestration skills + 13 domain skills = 23 distributable skills**. Unreleased development adds opt-in product discovery and an artifact-export utility without changing the v0.1 release tag.

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
| `shape` | Resolve product ambiguity, decisions, specs, opt-in product discovery, and wayfinding when needed. |
| `architect` | Make consequential architecture decisions and record tradeoffs. |
| `plan` | Produce implementation contracts with depth proportional to the work. |
| `implement` | Execute coherent feature slices implementation-first. |
| `accept` | Prove observable behavior with risk-appropriate evidence. |
| `debug` | Reproduce, isolate root cause, fix, and protect against regression. |
| `review` | Review the intended change with evidence-backed findings. |
| `finish` | Verify, reconcile, check diff hygiene, and produce closure/handoff evidence. |
| `continue` | Reconstruct current truth and resume the first eligible work. |

### Domain skills

| Skill | Purpose |
| --- | --- |
| `ui-engineering` | Surface-aware web/desktop/mobile/hybrid UI, responsive/adaptive behavior, accessibility, and visual craft. |
| `mobile-engineering` | Mobile lifecycle/background behavior, local-first/offline sync, device concerns, and native/hybrid boundaries. |
| `database-engineering` | Application data modeling, constraints, transactions, query shapes, and indexes. |
| `migration-engineering` | Safe current-to-target transitions, compatibility windows, reconciliation, cutover, and deprecation. |
| `api-design` | Consumer-facing HTTP/RPC/GraphQL/event/webhook contracts, failures, idempotency, and evolution. |
| `integration-engineering` | External-system boundaries, mapping, rate limits/retries, webhooks/polling, and reconciliation. |
| `async-work` | Background jobs, queues/events, ownership, acknowledgement, ordering, cancellation, replay, and backpressure. |
| `platform-engineering` | Workload-to-runtime/platform design, IaC/CI infrastructure, runtime configuration, and deployment topology. |
| `reliability-engineering` | Observability, dependency failure, graceful degradation, recovery evidence, and incident learning. |
| `security-engineering` | Trust boundaries, authentication/authorization, secrets, untrusted input, and evidence-based security review. |
| `privacy-engineering` | Purpose, minimization, retention, deletion, consent, telemetry, derived data, and AI-trace privacy. |
| `performance-engineering` | Measurement, profiling, optimization experiments, capacity/headroom, and cost tradeoffs. |
| `ai-engineering` | Provider-neutral LLM/AI contracts, structured outputs, tools, RAG, fallback, evals, and AI observability. |

Domain skills are normally composed by a core workflow from detected concerns; users do not need to invoke every specialist manually.

### Utility skills

| Skill | Purpose |
| --- | --- |
| `artifact-export` | Transform settled Proofcraft artifacts into external collaboration formats such as OpenSpec without changing canonical project truth or inventing missing decisions. |

Human-facing aliases include `discover` → `shape:discover` and `export` → `artifact-export:export`. Discovery remains opt-in; export runs only when explicitly requested. When discovery or shaping needs human decisions, questioning is adaptive by default, with explicit `single` and `batch` strategies available to trade conversational depth for speed.

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