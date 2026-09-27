# Cache and Derived State

Do not call state a cache until losing it is safe.

For cached/derived state define:
- authoritative source;
- derivation/rebuild path;
- invalidation owner;
- TTL/staleness bound;
- miss behavior;
- cache-unavailable behavior;
- write-path invalidation;
- stampede/backpressure concerns when material.

If loss or stale values change business correctness beyond an accepted bound, treat the dependency as authoritative or coordination state instead of hiding it behind the word cache.
