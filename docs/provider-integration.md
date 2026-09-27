# Provider Integration

Provider integrations are capability adapters, not architecture preferences.

Resolution order:

`task -> concern -> capability -> existing project technology -> available specialist -> provider`

Hard rules:

- Installed does not mean selected.
- Available does not mean appropriate.
- Existing project decisions win unless intentionally revisited.
- A provider may never silently select itself as the project's architecture.
- Core behavior must remain functional without a provider integration.

Examples include visual-design providers, Terraform specialists, database specialists, observability tools, browser automation, and model/AI SDK specialists.
