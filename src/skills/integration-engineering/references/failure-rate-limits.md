# Integration Failure and Rate Limits

For each external call, define:
- timeout/deadline;
- retryable vs permanent failure;
- idempotency/duplicate behavior;
- provider rate-limit semantics and backoff;
- circuit/open-loop behavior only when justified;
- partial/ambiguous outcome;
- fallback or degraded behavior.

Avoid synchronized retries and unbounded retry loops. Respect provider retry-after or quota signals when available.
