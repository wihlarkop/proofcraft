# Contributing

Edit canonical skill instructions under `src/skills/<name>/SOURCE.md` and shared references under `src/shared/`; never edit generated files under `skills/` directly.

`SOURCE.md` is deliberately not named `SKILL.md`. Only `skills/<name>/SKILL.md` is distributable/discoverable. This prevents installers from seeing duplicate paths for the same skill.

Before submitting a change:

```bash
python scripts/build.py
python scripts/validate.py
python scripts/check_generated.py
```

A change to behavior should include an eval that would have failed before the change. Keep skills focused, prefer references for techniques, and avoid adding a standalone skill unless the capability has a distinct trigger, workflow, output, and stop condition.
