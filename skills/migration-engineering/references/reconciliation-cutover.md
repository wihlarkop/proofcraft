# Reconciliation and Cutover

Before cutover, define how to prove source and target agree at the required semantic level. Row counts alone may not prove correctness.

A cutover should name:
- prerequisites;
- source of truth before and after;
- success signal;
- monitoring/evidence window;
- abort condition;
- rollback, roll-forward, or restore path;
- ownership;
- cleanup trigger.

Irreversible data transformation requires explicit recovery evidence rather than optimistic rollback language.
