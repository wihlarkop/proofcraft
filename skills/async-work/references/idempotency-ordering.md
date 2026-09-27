# Idempotency and Ordering

Assume retries can create duplicates unless the system proves otherwise.

Define:
- stable work/event identity;
- idempotency scope and retention;
- deduplication location;
- ordering scope (global, partition/key, entity, or none);
- behavior for late/out-of-order work;
- concurrency control around shared invariants.

Do not claim “exactly once” without specifying the boundary and evidence that makes duplicate effects impossible.
