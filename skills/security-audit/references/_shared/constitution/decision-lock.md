# Decision Lock

Do not reopen a settled decision merely because another option exists.

Treat an explicit user decision, accepted ADR, current product constraint, or established repository convention as locked unless at least one condition holds:

- new evidence invalidates an assumption;
- requirements changed;
- the user explicitly asks to revisit the decision;
- the decision creates a concrete blocker or safety/correctness problem.

When reopening a decision, state what changed and why the previous basis no longer holds. Never let a provider-specific skill silently reopen a provider-neutral architecture decision.
