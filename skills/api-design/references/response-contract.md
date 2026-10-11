# Response Contract

Apply the precedence in `references/_shared/engineering/failure-handling.md` first. Existing coherent, materially safe conventions win; the following envelope is a greenfield HTTP/JSON default, not an existing-project migration mandate.

## HTTP/JSON baseline

Prefer a structured base response/envelope when bootstrapping a new consumer-facing HTTP/JSON API with no convention. Make serialization, omission vs null, and field optionality explicit and adjustable for justified project needs; do not make every field mandatory in every response.

| Field | Meaning |
| --- | --- |
| `data` | Consumer payload/domain result. |
| `code` | Stable machine-readable application/result/error identity; part of the consumer contract when client behavior depends on it. |
| `message` | Human-readable text, never a machine classification contract. |
| `meta` | Pagination or other response metadata when materially relevant. |
| `errors` | Structured validation/sub-error information when materially relevant, with safe paths/identities/details. |
| `success` | Application-level outcome when the project uses it. A boolean alone cannot distinguish rejection from unresolved mutation. |
| `status_code` | When included, the actual transport HTTP status, never a conflicting pseudo-status. |

Conceptual example (HTTP 200):

```json
{
  "success": true,
  "status_code": 200,
  "code": "OK",
  "message": null,
  "data": {"id": "123"},
  "meta": null,
  "errors": null
}
```

Keep HTTP transport semantics separate from application/business outcome. Normal HTTP semantics are a valid default: a missing resource can be HTTP 404 with a stable code. If the project intentionally selects HTTP 200 for a valid business-level absence, use transport-consistent `status_code: 200`, `success: false`, `code: "USER_NOT_FOUND"` (when those fields are used). Never emit HTTP 200 with body `status_code: 404`, and never require all domain not-found outcomes to use HTTP 200. Preserve headers and native no-body responses such as HTTP 204/304; do not wrap downloads/streams mechanically.

Prefer one clear response-construction owner: a native generic response type/model, constructors, pagination metadata, validation representation, or framework response mechanism as needed. Avoid repeated endpoint dictionaries, but do not require helper calls when native responses are clearer. A name such as BaseResponse, particular files, or class hierarchy is not required.

**Complete the response path:** when the envelope carries an HTTP status, couple the actual transport status and serialized body field to the same boundary decision through the framework's native response/lifecycle mechanism or the project's established owner. An envelope field is not transport behavior; a helper returning only a body/model does not establish that coupling by itself. Before treating construction as complete, trace each selected status through actual response emission and body serialization, including non-default choices. Verify the response path rather than variable names or assignments to body fields. Native handling that already provides this relationship needs no extra wrapper.

## Protocol-native contracts

For gRPC use protobuf responses plus gRPC status/typed error details; for GraphQL preserve its `data`/`errors` semantics. Events/webhooks/streams use native delivery, acknowledgement, failure, retry, and reconciliation contracts. CLI uses exit codes and stdout/stderr, with structured output only when intended. Preserve stable identity, explicit outcomes, and translation ownership without imposing the JSON envelope on these protocols.
