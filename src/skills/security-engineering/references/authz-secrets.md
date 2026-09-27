# Authorization and Secrets

Authorization checks belong at the authoritative action/resource boundary and should derive identity from trusted authentication context.

For secrets:
- do not embed server credentials in browser/mobile binaries;
- scope privileges narrowly;
- prefer rotation/revocation capability;
- avoid secrets in logs/traces/errors;
- distinguish public client identifiers from server credentials.

A feature flag or hidden UI is not authorization.
