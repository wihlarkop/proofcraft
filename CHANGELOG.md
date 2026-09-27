# Changelog

All notable changes to Proofcraft are documented here.

## [0.1.0] - 2026-09-28

### Fixed
- `privacy-engineering` now distinguishes settled architecture from executable implementation readiness, preserving unresolved retention, deletion, consent/revocation, residency, and user-rights policy as explicit planning gates instead of allowing placeholder lifecycle defaults.
- Proofcraft's own repository guidance now enforces project-local repository truth before harness/global/personal memory during self-dogfood and release assessment.
- `debug` now stays the single core workflow owner, composes only material domain skills, respects investigation-only requests, distinguishes current facts/reproducers from hypotheses and not-yet-possible future states, and bounds runtime evidence collection instead of inventing a root cause.
- `shape` now closes only the human decisions actually answered, preserving adjacent unresolved product questions instead of silently collapsing related field scope, conflict, deletion, account-linking, or lifecycle policy.
- `finish` now remains the single core workflow owner, composes only material domain skills, reuses sufficient acceptance evidence instead of replaying earlier workflows, and keeps final evidence/blockers owned by handoff/readiness rather than duplicated across plan/context artifacts.
- `accept` now composes material domain verification skills, stays read-only unless repair is explicitly requested, distinguishes host evidence from device/runtime evidence, and prevents aggregate PASS wording when required criteria remain blocked or not run.
- `implement` now explicitly composes material domain skills, preserves open product decisions while allowing reversible implementation mechanisms, keeps sibling core workflows out of the implementation phase, and treats blocked runtime evidence and expected no-match cleanup probes cleanly.
- `setup` now places project-local-context and optional-Git bootstrap guards in the managed `AGENTS.md` guidance so they apply before task-specific skills load.
- `plan` now explicitly loads selected material domain skill contracts instead of treating broad skill-tree discovery as composition.
- `plan` now starts from project-local durable context, treats non-Git workspaces normally, refuses to invent unresolved product policy merely to complete a plan, and handles direct stale-context contradictions against accepted artifacts.
- `architect` and the shared reality-check now keep project-local context authoritative, avoid Git probes in non-Git workspaces, reconcile stale orientation after durable decisions, and preserve required architectural properties without prematurely freezing incidental encodings such as UUID.
- `shape` now keeps workspace-local artifacts authoritative over unrelated harness/global memory, avoids silently resolving material product ambiguity, and surfaces domain concerns without prematurely selecting implementation technology.
- Canonical authoring skill files now use `SOURCE.md` so installers discover exactly one `SKILL.md` path per skill; this fixes ambiguous project updates caused by duplicate `src/skills/*/SKILL.md` and `skills/*/SKILL.md` matches.
- `setup` now treats an empty non-Git folder as a first-class greenfield workspace, detects Git before Git-specific probes, and treats expected no-match searches as normal evidence rather than failed setup steps.

### Added
- Representative security/privacy dogfood evidence is recorded under `docs/dogfood/`, including the privacy-readiness regression that produced `privacy-engineering` 0.1.1.
- Mame v0.1 dogfood evidence is recorded under `docs/dogfood/` so release audits can distinguish materially exercised workflows from synthetic eval-only coverage.
- Proofcraft repository identity and initial public project structure.
- Canonical shared methodology layer and generated self-contained distribution model.
- All 10 core workflow skills: `setup`, `shape`, `architect`, `plan`, `implement`, `accept`, `debug`, `review`, `finish`, and `continue`.
- `ui-engineering` for surface-aware responsive/adaptive design, accessibility, WebView/hybrid guidance, durable `DESIGN.md` ownership, and optional Impeccable provider composition.
- `mobile-engineering` for lifecycle/background behavior, first-class local-first/offline sync, conflict resolution, mobile input/device concerns, hybrid boundaries, and mobile-specific verification.
- `database-engineering` for application data models, invariants, constraints, transactions, queries, and indexes.
- `migration-engineering` for compatibility windows, data movement, reconciliation, cutover/recovery, and safe contraction.
- `api-design` for explicit consumer-facing request, mutation, event, webhook, error, idempotency, and evolution semantics.
- `integration-engineering` for external-system mapping, failures, rate limits, webhook/polling choices, and reconciliation.
- `async-work` for background jobs/messages, durable ownership, acknowledgement, idempotency, ordering, cancellation, replay, and backpressure.
- `platform-engineering` for workload-first runtime, IaC/provider neutrality, runtime controls, and CI/deployment substrate concerns.
- `reliability-engineering` for question-first observability, resilience, degradation, recovery evidence, and incident learning.
- `security-engineering` for trust boundaries, authn/authz, secrets, untrusted input, threat modeling, and evidence-based security review.
- `privacy-engineering` for purpose/minimization, full data lifecycle, retention/deletion verification, telemetry, and AI trace privacy.
- `performance-engineering` for baseline/profile/experiment loops plus capacity and cost reasoning.
- `ai-engineering` for provider-neutral model contracts, structured output, tools, RAG, failure/fallback semantics, evals, and AI observability.
- Shared state-authority, lifecycle, synchronization, cache/derived-state, and design-artifact references.
- Stdlib-only build, validation, and generated-tree freshness checks.
- Per-skill eval fixtures plus suite-level routing, ceremony, and high-assurance cases.
- GitHub Actions validation for generated output and repository consistency.