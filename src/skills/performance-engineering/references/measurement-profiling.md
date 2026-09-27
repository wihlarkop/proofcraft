# Measurement and Profiling

Define the metric and workload before optimizing.

Prefer:
- end-to-end/user-journey timing for user-visible problems;
- representative production-like workload;
- profilers/traces/query plans to localize cost;
- repeated measurements where variance matters.

Control obvious confounders and compare the same metric before/after. A faster microbenchmark is not proof the product path improved.
