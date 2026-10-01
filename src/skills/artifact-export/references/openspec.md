# OpenSpec Adapter

Target the current OpenSpec `spec-driven` schema v1. OpenSpec is an interchange/collaboration target here, not a mandatory Proofcraft dependency.

## Detect existing OpenSpec structure

Before writing, inspect for:

- `openspec/config.yaml`;
- `openspec/specs/` capability paths;
- `openspec/changes/` and an explicitly targeted in-flight change;
- project-specific OpenSpec schema or rules when present.

When modifying an existing capability, reuse its exact path under `openspec/specs/`. Do not invent a near-duplicate capability name.

## Change layout

A normal `spec-driven` change lives under:

```text
openspec/changes/<change-name>/
├── .openspec.yaml
├── proposal.md
├── specs/
│   └── <capability-path>/
│       └── spec.md
├── design.md
└── tasks.md
```

Not every file must be exported. Generate only artifacts supported by settled Proofcraft sources.

For a newly created change, `.openspec.yaml` uses the project schema when already configured; otherwise the built-in target is `schema: spec-driven`. Target-format metadata such as the creation date may be generated normally.

## Proposal mapping

`proposal.md` explains WHY and WHAT changes. Map only settled source material into:

- `## Why` — existing problem, opportunity, or user outcome;
- `## What Changes` — settled behavioral scope;
- `## Capabilities` — new or modified capability paths;
- `## Impact` — only impact already established by current artifacts or repository evidence.

If the source has no trustworthy motivation/scope needed for a proposal, do not invent it.

## Delta spec mapping

Create one `specs/<capability-path>/spec.md` per affected capability.

Use only the operation that is supported by the source and existing OpenSpec state:

- `## ADDED Requirements` for genuinely new requirements;
- `## MODIFIED Requirements` when an existing requirement behavior changes;
- `## REMOVED Requirements` when an existing requirement is explicitly removed;
- `## RENAMED Requirements` when a requirement rename is explicitly decided.

Requirements describe observable WHAT, not implementation HOW.

Use OpenSpec scenarios in this form when the Proofcraft behavior can be expressed observably:

```markdown
### Requirement: Low-stock threshold
The system MUST allow a consumable inventory item to have a low-stock threshold.

#### Scenario: Stock falls below threshold
- **WHEN** available quantity falls below the configured threshold
- **THEN** the item is considered low stock
```

Preserve explicit failure, compatibility, security, privacy, and lifecycle semantics when they are part of the behavioral contract.

## Design mapping

Create `design.md` only when Proofcraft already has settled technical design material worth exporting, such as consequential ADR decisions or a substantial implementation approach.

Map without duplicating behavioral requirements:

- Context;
- Goals / Non-Goals when design-specific;
- Decisions and rationale;
- Risks / Trade-offs;
- Migration Plan when present;
- genuinely deferrable Open Questions.

Do not turn unresolved product questions into design open questions.

## Tasks mapping

Create `tasks.md` only from an existing implementation plan or equivalent settled task breakdown. Preserve dependency/order semantics where material and use OpenSpec checkbox task syntax.

Do not decompose the implementation from scratch merely because OpenSpec normally has `tasks.md`.

## Validation

If an OpenSpec CLI is already available, use its current validation command against the exported change and report the result. If it is unavailable, do not install it unless the user asks; report that native OpenSpec validation was not run.

## Authority

The export does not silently change authority. Proofcraft canonical artifacts remain authoritative unless the repository or user explicitly adopts OpenSpec as the canonical specification system.
