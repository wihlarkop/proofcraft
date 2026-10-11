# Errors, Preconditions, and Idempotency

Make failure behavior machine-usable, following `response-contract.md` and the shared failure-handling precedence/ownership contract.

For the relevant operations, define stable code/type, public details, transport mapping, outcome certainty, and consumer recovery. Cover these categories proportionally; the table is guidance, not a mandatory error hierarchy or universal status policy:

| Failure | Contract/recovery concern |
| --- | --- |
| Validation | Safe field/sub-error details; correct input before resubmission (commonly HTTP 400/422). |
| Authentication | Establish/renew credentials (commonly 401); preserve protocol-required challenge headers. |
| Authorization | Permission failure (commonly 403), or resource hiding where required. |
| Not found | Identify the intended recovery without disclosing forbidden resource state (commonly 404). |
| Conflict / stale revision | Reconcile current state/preconditions, preserve drafts (commonly 409/412); no blind overwrite. |
| Invariant / business rejection | Explicit application rejection code; transport follows the selected contract. |
| Rate limit | Bounded backoff and retry timing where known (commonly 429/Retry-After). |
| Dependency unavailable | Degradation/recovery policy (often 503); mutation outcome may still be unresolved. |
| Timeout | Deadline and recovery semantics; lack of a response is not evidence of non-application. |
| Unexpected / internal | Safe generic public response (commonly 500), useful internal diagnostics. |
| Ambiguous / unresolved mutation | Preserve original operation identity until authoritative evidence resolves it. |

When clients need different recovery for failures sharing a status, expose distinct stable machine-readable identities. HTTP 404 + `RESOURCE_NOT_FOUND` can mean refresh a removed row, while HTTP 404 + `MAKE_DO_DEFINITION_NOT_FOUND` can mean repair a missing activity prerequisite. Clients must not parse messages; authorization/resource-hiding policy still outranks specificity.

For mutations define idempotency-key scope/retention, payload matching, receipt/result retrieval, concurrency/version preconditions, partial outcomes, and retry safety. Keep SUCCESS, DEFINITIVELY REJECTED, and OUTCOME UNKNOWN / UNRESOLVED separate as defined by the shared failure-handling contract. A later failed retry does not resolve a lost original response. Do not tell consumers to “just retry” unless duplicate side effects are safely bounded.
