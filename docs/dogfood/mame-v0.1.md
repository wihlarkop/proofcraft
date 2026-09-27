# Mame v0.1 Dogfood Evidence

Status: completed exploratory dogfood cycle for the Proofcraft v0.1 release-candidate assessment.

This record captures what was materially exercised through the Mame workspace so later release audits can distinguish real dogfood evidence from synthetic prompt fixtures. It is evidence about Proofcraft behavior, not Mame product roadmap.

## Test project

Mame is a small Flutter + SQLite save-for-later application used to exercise Proofcraft across a realistic project lifecycle. The dogfood intentionally included greenfield setup, product shaping, architecture, planning, implementation, acceptance, closure, continuity, migration planning, review, debugging, and post-dogfood reconciliation.

The Mame workspace itself was non-Git during the cycle. Proofcraft changes discovered during dogfood were committed to this repository.

## Core workflow coverage

All 10 core workflows were materially exercised.

| Core skill | Dogfood outcome | Resulting Proofcraft hardening |
| --- | --- | --- |
| `setup` | Greenfield/non-Git onboarding and bootstrap context behavior exercised. | Non-Git handling and project-local bootstrap guards were hardened. |
| `shape` | Product ambiguity, future sync exploration, and single-decision-frontier shaping exercised. | Project-local context and decision-boundary handling were hardened; adjacent unanswered decisions are now preserved. |
| `architect` | Flutter + SQLite architecture selection and durable-property boundaries exercised. | Project-local reality checks, decision lock, and avoiding premature mechanism lock-in were hardened. |
| `plan` | First usable slice and later sync planning exercised. | Project-local context, non-Git behavior, domain composition, and anti-invention guards were hardened. |
| `implement` | First usable Flutter/SQLite vertical slice implemented. | Domain composition, open-decision preservation, blocked runtime evidence, and single-core ownership were hardened. |
| `accept` | Host-verifiable acceptance plus blocked phone/runtime evidence exercised. | Domain composition, read-only default, evidence boundaries, and aggregate blocked/not-run semantics were hardened. |
| `debug` | Hypothetical future-schema startup report investigated without implementing a fix. | Single-core ownership, investigation-only behavior, future-state falsification, and bounded runtime evidence were hardened. |
| `review` | SQLite migration dogfood plan reviewed read-only against repository evidence. | Clean pass; no contract patch was required. |
| `finish` | First usable slice closure, readiness, and artifact reconciliation exercised. | Single-core ownership, evidence reuse, artifact ownership, and blocked-readiness semantics were hardened. |
| `continue` | Fresh-session continuity exercised with only “Continue the Mame project.” | Clean pass; no contract patch was required. |

A later fresh-session smoke test correctly reconstructed implemented behavior, accepted architecture, committed product direction, next eligible work, and dogfood-only materials after cleanup.

## Domain coverage

Material domain evidence from the Mame cycle is narrower than the full 13-skill surface.

- `mobile-engineering`: exercised around local-first/offline behavior and device/runtime evidence boundaries. Real phone/emulator runtime remained blocked, so this is not full mobile-runtime validation.
- `database-engineering`: exercised against the actual SQLite repository, schema authority, identity, persistence, and debugging boundaries.
- `migration-engineering`: materially exercised through a read-only hypothetical SQLite schema-evolution plan and a subsequent evidence-based review.
- `async-work`: touched during future multi-device sync shaping as a relevant concern, but not materially exercised through implementation/runtime behavior.

The remaining domain skills should not be described as materially dogfooded by Mame solely because synthetic eval fixtures exist. Security and privacy were later exercised separately in `docs/dogfood/security-privacy-v0.1.md`. Platform, reliability, performance, AI, and external integration/API contracts still need representative real-work exercise when release confidence depends on those claims.

## Dogfood-derived fixes

The Mame cycle directly motivated the following hardening commits in Proofcraft history:

- `074663` — non-Git setup behavior.
- `517ed4` — project-local shaping behavior.
- `5d18745` — architecture reality-check and durable-property handling.
- `f70be03`, `168a26` — planning guards and domain composition.
- `17d94c7` — bootstrap project-local context guards.
- `4a985a3` — implementation domain composition and evidence handling.
- `aa71d89`, `826b3a1` — acceptance hardening and generated sync.
- `2ce29ed`, `29286db` — finish ownership/reconciliation hardening and generated sync.
- `70d871c`, `b26e81a` — shaping decision-boundary hardening and generated sync.
- `ffb480b` — evidence-driven debugging hardening.

This list is intentionally evidence-oriented rather than a complete repository changelog.

## Release-assessment interpretation

For v0.1 release-candidate assessment:

- The full core lifecycle has real dogfood coverage, although not every workflow required a post-dogfood patch.
- Synthetic eval presence is not equivalent to material dogfood.
- Mame materially validates only a subset of domain concerns.
- A release audit should use this record together with current source, generated-tree validation, Git/CI state, and the changelog; this record never overrides newer repository truth.