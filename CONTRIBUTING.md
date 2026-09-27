# Contributing

Edit canonical files under `src/`; never edit generated files under `skills/` directly.

Before submitting a change:

```bash
python scripts/build.py
python scripts/validate.py
python scripts/check_generated.py
```

A change to behavior should include an eval that would have failed before the change. Keep skills focused, prefer references for techniques, and avoid adding a standalone skill unless the capability has a distinct trigger, workflow, output, and stop condition.
