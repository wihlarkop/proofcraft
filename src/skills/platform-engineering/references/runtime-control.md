# Runtime Configuration and Feature Flags

Distinguish configuration from behavioral rollout controls.

For flags/kill switches define:
- purpose and owner;
- safe default/fallback;
- targeting scope;
- auditability;
- production-intended and fallback-state tests;
- expiry/cleanup for temporary flags.

Flags control future code paths; they do not undo schema mutations, already-written data, sent messages, payments, or other external side effects.
