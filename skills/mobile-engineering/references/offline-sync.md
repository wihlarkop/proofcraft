# Offline Synchronization

For offline-capable writes, prefer a durable local mutation record with stable client-generated identity so retries/replay are idempotent.

Define:
- upload ordering requirements;
- retry/backoff and connectivity triggers;
- remote-change cursor/version strategy;
- partial sync scope;
- deduplication;
- interrupted-sync recovery;
- reconciliation after success/failure;
- cleanup/compaction of acknowledged local work.

A sync engine must tolerate retries and app restarts without silently duplicating or losing accepted work.
