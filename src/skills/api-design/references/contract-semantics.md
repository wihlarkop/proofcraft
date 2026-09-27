# Contract Semantics

For consumer-visible data, define:
- identifiers and stability;
- required/optional fields;
- absent vs null;
- defaults;
- enum evolution;
- timestamps, time zones, and units;
- ordering;
- filtering/search;
- pagination/cursors;
- validation limits.

Ambiguous semantics become consumer coupling. Prefer explicit contracts over behavior inferred from current implementation.
