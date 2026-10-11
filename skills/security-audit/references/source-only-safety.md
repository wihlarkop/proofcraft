# Source-Only Audit Safety

M1 audits untrusted repositories without executing target-controlled code. “Read-only” describes how source is inspected; it does not make execution safe.

Do not automatically invoke target build or install scripts, dependency lifecycle hooks, test suites, application commands, untrusted binaries, production requests, or exploit payloads. A test command can execute arbitrary repository code. Report the runtime evidence that would strengthen a candidate and leave that check unresolved or blocked unless a separate, verified sandbox is available.

The bundled validate_audit.py is trusted Proofcraft tooling. It parses JSON and checks that referenced source/evidence files exist beneath the supplied roots. It must not import, evaluate, or execute any target file. Its structural validation does not prove exploitability, source authenticity, or genuine reviewer independence.

Use a separate verifier with fresh context or a distinct reviewer when available. Record its conclusion as supports, refutes, or inconclusive, distinct from the explanation of its result. Only a supportive conclusion can accompany a confirmed finding; a refutation should reject the candidate when the evidence resolves it, while unresolved disagreement or inconclusive verification remains visible as needs_validation. If independent capability is unavailable, retain a supported hypothesis as needs_validation; never fabricate an agent, reviewer, identity, or verification result.

M2’s OS-enforced sandbox, restricted network, credential isolation, resource limits, and trusted artifact promotion are not provided by M1. .proofcraft/, a separate directory, and a model’s stated intent are not sandbox controls.
