---
name: setup
description: >-
  Initialize or reconcile repository operating context for coding agents. Use for a fresh
  repository, first-time project onboarding, a materially changed project structure, or an
  explicit request to create/reconcile AGENTS.md and project context. Preserve existing human
  instructions; do not invent undecided architecture or mutate a repository merely because the
  suite was updated.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Setup

Establish the minimum durable context an agent needs to work safely in a repository.

## Trigger

Use for greenfield repository initialization, first-time onboarding after this suite is installed, explicit AGENTS/project-context reconciliation, or a material project/tooling reorganization.

Do not use for normal feature work.

## Workflow

1. Read the relevant shared constitution and run a focused reality check.
2. Classify the repository as greenfield or existing.
3. Inspect existing `AGENTS.md`, repository layout, manifests, task runners, docs, ADR/product/design artifacts, CI configuration, and obvious optional specialist capabilities. Do not exhaustively inventory the repository when a pointer is enough.
4. For greenfield projects, create only minimum navigation/context. Leave undecided architecture explicitly undecided.
5. For existing projects, preserve established conventions and human-authored instructions. Manage only the marked block in `AGENTS.md` when one is created.
6. Keep `AGENTS.md` thin; point to canonical context instead of copying large instructions.
7. Record the workflow schema and suite-major compatibility in project context when this project adopts the suite.

## Outputs

Normally:
- a thin `AGENTS.md` managed block;
- `docs/agents/project.md` or the repository's established equivalent;
- an ADR directory/convention only when one does not exist and architecture decisions are expected.

Do not create fake product, design, or architecture decisions just to populate files.

## Stop

Stop when the project is navigable, human content is preserved, canonical sources are discoverable, and no invented decision has been introduced.
