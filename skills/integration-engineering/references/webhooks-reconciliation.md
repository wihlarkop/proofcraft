# Webhooks, Polling, and Reconciliation

Webhooks are notifications, not automatically authoritative truth.

Define:
- authenticity/verification handoff to security;
- event identity and deduplication;
- ordering assumptions;
- acknowledgement timing;
- retry behavior;
- what happens when delivery is missed;
- whether polling/backfill/reconciliation is required;
- source of truth after ambiguous outcomes.

A robust integration can explain how it converges after missed, duplicated, delayed, or reordered external notifications.
