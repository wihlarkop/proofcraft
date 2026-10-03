# Verification Surfaces

Choose evidence that reaches the interface or runtime surface where the claim can actually fail. Test shape follows product and protocol semantics; there is no universal test pyramid or mandatory runner.

## Selection rules

- Start from the observable claim and ask what evidence could falsify it.
- Reuse the project's existing supported runner, client, harness, emulator, fixture, or protocol tooling. For example, a repository that already uses Playwright for browser journeys should normally extend Playwright rather than add Cypress or a second browser stack.
- Static/type/lint/build checks prove source or build properties. They do not prove rendered interaction, network transport, database semantics, or device behavior.
- Prefer the narrowest direct evidence that crosses the material boundary. Escalate to broader E2E only when the behavior spans boundaries that narrower evidence cannot establish together.
- A mock or stub proves only the behavior encoded by that fake. Do not use it as evidence for a real provider, transport, browser, database engine, or device guarantee it does not exercise.
- When verification writes external state, apply the test-environment-isolation contract before running it.

## Browser and UI

Use rendered/runtime evidence for user-visible interaction claims.

- Exercise the actual user journey, relevant state transitions, validation/error/loading states, focus and keyboard behavior, and the viewport/input modes material to the product.
- When browser automation is appropriate, prefer the project's existing runner such as Playwright, Cypress, or WebDriver and use its native locator, trace, screenshot, network, and accessibility-relevant capabilities instead of creating parallel wrappers.
- Screenshots are useful visual evidence but do not prove that an interaction, submission, focus transition, or async state change works. Pair them with interaction/DOM/runtime evidence for behavioral claims.
- Visual regression snapshots are not a default requirement. Use them when the visual contract is intentionally stable enough that the maintenance cost is justified; otherwise inspect representative rendered states directly.
- Treat SSR/hydration, responsive behavior, pointer/touch, dark/light themes, or reduced motion as material only when the application and claim actually depend on them.

## HTTP, REST, and GraphQL

Verify the consumer-visible contract and the runtime behavior that matters.

- Check request/input validation, response/data shape, identifiers and null/absence semantics, authentication/authorization, error representation, and status/result semantics.
- For mutations, exercise material idempotency, concurrency/precondition, retry, and partial-failure behavior rather than checking only a happy 2xx response.
- Check pagination/filtering/ordering when consumers rely on them.
- For GraphQL, include operation/schema compatibility and material partial-data/error semantics rather than forcing HTTP resource conventions onto the graph.
- Use generated/open schema checks where they protect compatibility, but exercise the real handler/transport and relevant backing integration when the claim depends on runtime behavior.

## RPC and gRPC

Test RPC semantics as RPC semantics rather than translating them into an HTTP checklist.

- Verify IDL/protobuf and generated-client compatibility where applicable.
- Exercise request/response and status/error semantics, metadata, deadlines/timeouts, cancellation, and retry/idempotency behavior when material.
- For client-, server-, or bidirectional streaming, verify ordering, termination, backpressure/cancellation, and partial-failure behavior relevant to the contract.
- Use an actual client/server transport boundary when transport behavior is part of the claim; pure handler tests do not prove framing, metadata, deadlines, or streaming behavior.

## Events, streams, and webhooks

Verify the delivery contract that consumers actually depend on.

- Exercise duplicate, ordering, retry/redelivery, gap/replay, acknowledgement, and idempotency semantics where applicable.
- Verify authentication/signature and payload compatibility for webhooks when they are part of the boundary.
- Test reconciliation when correctness depends on recovering missed, delayed, or ambiguous deliveries.

## Persistence and migrations

Use the real database/storage engine when claiming engine-specific behavior.

- Verify constraints, transactions, rollback, isolation/locking, concurrency, migration compatibility, and query semantics at integration level when those guarantees matter.
- Pure domain tests remain useful for deterministic rules but do not prove PostgreSQL/SQLite/MySQL-specific behavior.
- Keep destructive or accumulating cases on a disposable/isolated target with bounded cleanup.

## CLI and process boundaries

For command-line behavior, verify exit status, stdout/stderr contract, file/process side effects, invalid input, and interruption/cancellation where material. Parsing unit tests do not establish process-level behavior by themselves.

## Mobile, desktop, and device runtimes

Host tests prove only host-verifiable behavior. Use the actual emulator/device/window/runtime when the claim depends on platform lifecycle, native integration, permissions, input, rendering, filesystem, audio, networking, backgrounding, or other platform behavior. Report unavailable runtime evidence as BLOCKED rather than substituting a different platform.

## Regression scope

After a failure is fixed, rerun the failed scenario plus the smallest affected regression subset. Expand only when evidence indicates wider coupling or risk; do not reflexively rerun every suite or stop at a narrow assertion that misses the real boundary.
