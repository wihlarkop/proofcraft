# Transaction Boundaries

A transaction should protect one atomic invariant, not merely group nearby statements.

Ask:
- what must commit together?
- what must never become visible partially?
- what concurrent operation can violate the invariant?
- what retry behavior exists after an ambiguous failure?
- what external side effect cannot participate in the database transaction?

Keep transactions as small as correctness permits. When state change and message publication must be atomic across boundaries, report an async/messaging concern such as an outbox rather than pretending a remote call is transactional.
