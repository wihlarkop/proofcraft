---
name: migration-engineering
description: >-
  Plan or review safe transitions from a current system/state to a target state across schemas,
  data stores, APIs, infrastructure, or service ownership. Use when old and new states must coexist,
  data/backfill/reconciliation is required, consumers migrate over time, or cutover/deprecation has
  meaningful risk. Make compatibility windows, irreversible steps, recovery, and cleanup explicit.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Migration Engineering

A migration is a controlled transition, not just the target design.

## Workflow

1. Describe current state, target state, invariants that must survive, and the populations/versions that may coexist.
2. Identify additive/compatible expansion that allows old and new behavior to operate safely.
3. Define data movement/backfill, dual-read/write or translation behavior only when necessary.
4. Define verification and reconciliation before cutover.
5. Bound the cutover: entry conditions, success signal, abort/recovery path, and operator responsibility when relevant.
6. Delay destructive contraction until evidence shows old consumers/state are gone.
7. Mark irreversible steps explicitly. Do not promise rollback where only roll-forward or restore is credible.
8. Route schema/query implementation to database-engineering, contract semantics to api-design, platform mechanics to platform-engineering, and recovery evidence to reliability-engineering as needed.

## Stop

Stop when transition sequencing, compatibility, reconciliation, failure handling, and cleanup/deprecation conditions are explicit enough to execute safely.
