# Query and Index Review

Optimize from observed access patterns.

Inspect:
- filter predicates;
- join keys;
- ordering;
- pagination;
- cardinality/selectivity;
- read/write frequency;
- representative query plans when performance matters.

Indexes trade read speed for write/storage/maintenance cost. Avoid speculative indexes without a query they serve. For performance incidents, measure before and after and compose performance-engineering when profiling/benchmarking is the primary task.
