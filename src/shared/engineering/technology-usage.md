# Current Technology Usage

Use a selected language, runtime, framework, library, database, build tool, or developer tool through the current supported semantics and idioms of the version the project actually uses.

## Inspect first

- Read project-local manifests, lockfiles, version files, configuration, accepted architecture, and nearby working patterns before choosing a usage pattern.
- Prefer an established project convention when it remains supported and fits the accepted architecture.
- When correct usage is version-sensitive, unfamiliar, or materially changed across releases, consult current primary documentation, migration guidance, or maintainer examples for the selected version instead of relying on remembered examples.
- Research only the capability being used; do not turn implementation into a broad documentation survey.

## Honor semantic contracts

- Treat idiomatic usage as more than syntax or style. Choose APIs and constructs according to the actual contract: required versus optional presence, recoverable absence versus invariant failure, owned versus borrowed/resource-scoped lifetime, sync versus async execution, mutable versus immutable state, transaction ownership, and other semantics the technology exposes.
- Prefer the technology's explicit absence/error/state mechanisms when absence, failure, or alternatives are valid runtime states. Conversely, do not use permissive or fallback APIs where a missing value should expose a broken internal invariant.
- When a value obtained through an optional/fallible lookup is required downstream, validate or narrow it explicitly rather than letting an ambiguous null/none/undefined/default value propagate.
- Do not transplant habits from another language or framework when the selected ecosystem has a clearer native mechanism. A pattern that is conventional elsewhere is not automatically good practice here.
- Preserve stable shapes with the project's normal typed/modeling mechanism when that reduces ambiguity; do not replace a clear typed boundary with loose maps/objects merely for convenience, and do not introduce heavyweight modeling for genuinely ad-hoc data.

## Implement idiomatically

- Prefer current supported APIs and configuration over deprecated APIs, legacy compatibility shims, or patterns retained only from older versions.
- Respect the technology's intended ownership, lifecycle, extension, and composition boundaries instead of reproducing habits from another ecosystem.
- Use framework extension points and lifecycle hooks only when they own the behavior; do not wrap native mechanisms merely to make every technology look structurally identical.
- Use the selected package manager, formatter, linter, type checker, migration tool, code generator, and build tool through their normal supported workflows rather than emulating a different tool.
- Respect tool-owned generated artifacts, lockfiles, configuration precedence, cache/state directories, and update workflows instead of bypassing them with manual copies or parallel representations.
- If the project explicitly chose pre-stable or experimental tooling, honor that decision, follow its current documented workflow, and account for known limitations rather than silently replacing it.

## Native response and failure mechanisms

Preserve response/failure semantics using the selected technology's error model, ownership, lifecycle, and extension points. Inspect the project/version first; these are possible shapes, not required layouts or dependencies. Never structurally translate a Python example into another ecosystem.

- **Python/FastAPI:** a Pydantic generic response model when useful and typed application/domain exceptions where classification needs them. Keep native request validation. If validation is standardized into the selected envelope, register a FastAPI/Starlette HTTP-boundary handler for `RequestValidationError` and normalize allowlisted safe locations, codes, and public details; do not return raw request bodies, rejected inputs, framework context, or internal/debug details. Internal/model validation bugs are not consumer request failures. An intentionally accepted native validation contract needs no custom handler, but the greenfield envelope default must include request-validation translation rather than leave a second accidental shape. No required filenames or deep exception hierarchy. See [FastAPI error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/).
- **Go:** ordinary returned errors; `errors.New` sentinels, `%w` wrapping, `errors.Is`/`errors.As`, and concrete typed errors when structured information is needed. One HTTP response/error writer or native framework boundary owns translation. Handle serialization/write errors there or propagate them to an owner that can act. With `net/http`, headers or the first body write can commit the response: distinguish pre-commit failures from delivery failures, and do not attempt to send a replacement status/body after commitment. Use viable return, diagnostic, or connection-ending behavior for the selected server/framework rather than discarding errors or requiring one universal writer. Never simulate Python exception inheritance. See [Go error values](https://go.dev/wiki/ErrorValueFAQ) and [net/http response semantics](https://pkg.go.dev/net/http#ResponseWriter).
- **Rust:** fallible domain/application operations use `Result<T, E>` with normal `?`, `match`, or equivalent propagation. Keep concrete errors inspectable while downstream domain decisions, retry classification, HTTP/API mapping, or client behavior need to distinguish failure kinds; conversions/context must preserve that identity until classification. Framework conversion such as Axum `IntoResponse` belongs at the transport boundary. Opaque contextual errors are appropriate only where callers need propagation/diagnostics without concrete classification, often at startup/orchestration boundaries. Manual error implementations and custom mechanisms are valid: `thiserror` is optional, and `Box<dyn Error>`, custom opaque wrappers, `eyre`, or `anyhow` can serve opaque boundaries without requiring any of them. Do not erase required identity before its classifier or stringify errors for matching. See [Rust Result propagation](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html), [thiserror](https://docs.rs/thiserror/latest/thiserror/), [anyhow](https://docs.rs/anyhow/latest/anyhow/), and [Axum response conversion](https://docs.rs/axum/latest/axum/response/trait.IntoResponse.html).
- **TypeScript/Node:** use the selected framework's mechanism, such as [Fastify error handlers](https://fastify.dev/docs/latest/Reference/Server/#seterrorhandler), [Nest exception filters](https://docs.nestjs.com/exception-filters), or [Express error middleware](https://expressjs.com/en/guide/error-handling/), with typed results/discriminated unions where natural. Do not invent BaseController for ecosystem symmetry.
- **Other stacks/protocols:** inspect their native mechanisms rather than cargo-culting these examples. The greenfield JSON envelope belongs to HTTP/JSON; gRPC, GraphQL, events, streams, webhooks, and CLI retain native response/failure contracts.

### Rust bootstrap: connect the failure path

For a selected greenfield Rust HTTP stack, establish one representative failure path end to end as part of the foundation, including in a source rehearsal:

1. Implement a realistic fallible operation with a failure-producing branch and `Result<T, E>` return. Request parsing/validation can supply this without selecting persistence, inventing domain policy, or registering a demo endpoint.
2. Show its caller invoking that operation and propagating or handling the result using normal Rust flow. Keep the concrete error available wherever classification is still needed; any conversion must retain the distinctions the next owner consumes.
3. Connect that same propagated error to the selected framework's HTTP integration, where variants determine the chosen transport status and stable consumer code/type. Show how the caller's error actually reaches this boundary, not an unrelated enum/converter beside a plain-value call path.

Before considering bootstrap complete, trace an actual failure branch from operation through caller to contract mapping. An enum, a response conversion implementation, signatures alone, or a promise to add fallible flow later does not establish that path. A helper and HTTP-facing caller can suffice; do not add service hierarchies, exception-style handling, wrappers around `Result`, or an unused opaque orchestration layer to demonstrate it.

## Avoid cargo-cult best practices

- A recommendation is not a requirement merely because it is popular or appears in a template.
- Distinguish correctness/semantic guidance from subjective style. Prefer formatter/linter enforcement for mechanical style and reserve human/agent findings for choices that materially affect clarity, correctness, ownership, compatibility, or maintainability.
- Do not introduce repositories, service layers, factories, dependency-injection frameworks, event buses, caches, wrappers, or other abstraction layers without a concrete project problem they solve.
- Do not rewrite clear working code solely to match a stylistic preference or generic checklist.
- Existing architecture and project-local conventions outrank generic examples unless they are incompatible, deprecated, insecure, or directly contradicted by accepted project truth.

## Verify

Use the cheapest strong evidence appropriate to the changed technology surface: static diagnostics, build checks, focused runtime checks, integration evidence, or observable acceptance behavior. Verification is required; a particular test style is not.
