# Changelog

All notable changes to Proofcraft are documented here.

## [Unreleased]

### Fixed
- `shape` now keeps workspace-local artifacts authoritative over unrelated harness/global memory, avoids silently resolving material product ambiguity, and surfaces domain concerns without prematurely selecting implementation technology.
- Canonical authoring skill files now use `SOURCE.md` so installers discover exactly one `SKILL.md` path per skill; this fixes ambiguous project updates caused by duplicate `src/skills/*/SKILL.md` and `skills/*/SKILL.md` matches.
- `setup` now treats an empty non-Git folder as a first-class greenfield workspace, detects Git before Git-specific probes, and treats expected no-match searches as normal evidence rather than failed setup steps.

### Added
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