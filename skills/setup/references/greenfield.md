# Greenfield Setup

A greenfield project may be an empty ordinary folder or a Git repository. Detect that distinction before running Git-specific checks; source control is optional unless the user or existing workspace establishes it.

Installed agent tooling such as `.agents/` and a skills lockfile does not by itself make the workspace an existing application.

Initialize navigation rather than pretending architecture already exists. Record known facts, create a thin AGENTS managed block and project-context location, establish an ADR convention when useful, and leave stack/provider/architecture choices undecided until shaping or architecture work actually selects them.

Treat expected absence as information. Empty file searches, missing manifests, and “not a Git repository” should be handled as normal greenfield evidence rather than surfaced as failed setup steps.

## Selected backend foundation

Bootstrap includes response/error handling without a separate human reminder when the consumer-facing protocol and backend stack are already selected. With no consumer-facing backend/API, skip this concern. With either choice undecided, record it as open and do not invent a protocol, framework, or backend merely to establish the foundation.

For selected HTTP/JSON, compose `api-design` and load its response-contract and errors/idempotency references. Prefer the structured base envelope with project-adjustable optionality, one clear native response-construction owner, and one application-failure-to-transport translation boundary. Use the shared engineering references `failure-handling.md` and `technology-usage.md`: establish classification/recovery policy proportionally without generating unused error hierarchies, endpoint catalogs, or service/controller/repository layers. Other protocols keep their native contracts.

Complete the selected native boundary behavior, not just response/error declarations: framework request-validation paths must follow the adopted contract, and translation hooks must be wired. When a frontend is present, establish response-consuming decoding/classification behavior that exposes stable identities to features; types or a comment promising a future decoder do not complete bootstrap. Use the shared native-usage and failure-handling guidance for these mechanisms; presentation remains feature-owned.

Record the chosen contract and collect the cheapest useful evidence for representative success/failure and request-validation mapping, actual HTTP/body status consistency, and frontend decoding when present; add outcome/recovery coverage when the bootstrap contains mutations. Setup is not a full application generator and does not require a demo domain or unused dependencies.
