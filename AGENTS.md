# Agent Guide

This repository authors a portable Agent Skills suite.

## Source of truth

- Edit `src/skills/` and `src/shared/`.
- `skills/` is generated; do not hand-edit it.
- Run `python scripts/build.py` after source changes.
- Run `python scripts/validate.py` and `python scripts/check_generated.py` before considering work complete.

## Working rules

- Preserve unrelated working-tree changes.
- Keep the core vendor-neutral and harness-neutral.
- Provider integrations are optional enhancements, never architecture defaults.
- Do not turn techniques such as retry, TDD, state machines, or design patterns into standalone skills unless their boundary genuinely becomes independent.
- Add regression evals for real failures and over-triggering.
