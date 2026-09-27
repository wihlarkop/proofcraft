# Agent Guide

This repository authors a portable Agent Skills suite.

## Source of truth

- Edit canonical skill instructions in `src/skills/<name>/SOURCE.md` and shared methodology in `src/shared/`.
- Canonical authoring files are intentionally named `SOURCE.md`, not `SKILL.md`, so Agent Skills installers discover only the generated distribution.
- `skills/` is generated; do not hand-edit it.
- Run `python scripts/build.py` after source changes.
- Run `python scripts/validate.py` and `python scripts/check_generated.py` before considering work complete.

## Working rules

- Treat this repository, its current Git history, and its durable artifacts as authoritative for Proofcraft project facts.
- Do not consult harness-wide, global, or personal memory for Proofcraft project facts unless the user explicitly asks to reuse it or this repository points to it. If such memory is reused, verify it against current repository truth before making claims or durable changes.
- Preserve unrelated working-tree changes.
- Keep the core vendor-neutral and harness-neutral.
- Provider integrations are optional enhancements, never architecture defaults.
- Do not turn techniques such as retry, TDD, state machines, or design patterns into standalone skills unless their boundary genuinely becomes independent.
- Add regression evals or structural validation for real failures and over-triggering.
