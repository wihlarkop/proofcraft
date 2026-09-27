# External Boundary Mapping

Create an anti-corruption boundary when external concepts do not match the application's domain.

Map explicitly:
- external IDs to internal IDs;
- external status/lifecycle to internal state;
- optional/unknown fields;
- units/time zones;
- ownership of canonical truth;
- provider-specific errors into internal failure categories.

Preserve raw provider details only where needed for auditing/debugging. Do not spread vendor DTOs across unrelated domain code.
