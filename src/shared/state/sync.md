# Synchronization Semantics

Define synchronization from authority and failure behavior, not from a library choice.

Clarify:
- local and remote authority;
- sync direction;
- mutation identity and idempotent replay;
- ordering requirements;
- pull cursor/version semantics;
- conflict detection and resolution;
- retry/backoff and offline duration;
- partial sync behavior;
- reconciliation after interrupted sync;
- user-visible sync state when it affects decisions.

Never hide conflict semantics behind vague “last write wins” language unless that behavior is explicitly acceptable.
