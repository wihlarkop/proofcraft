# Acceptance Contract

Acceptance criteria are observable product claims. Express scenarios with precondition, action, and expected outcome when that structure adds clarity.

Verdicts:

- PASS — direct evidence satisfies the criterion.
- FAIL — direct evidence contradicts the criterion.
- BLOCKED — required evidence cannot currently be collected.
- NOT RUN — not yet executed; never treat as pass.

When a scenario fails, fix the defect, rerun the failed scenario, then run the affected regression subset rather than mechanically rerunning every possible check.
