# Telemetry and AI Trace Privacy

Telemetry and agent/LLM traces can contain user content, identifiers, tool arguments/results, prompts, and sensitive context.

Apply:
- purpose limitation;
- collection minimization;
- redaction before durable storage where possible;
- retention appropriate to debugging/evaluation need;
- deletion propagation;
- consent/notice requirements supplied by product/legal policy;
- separation of production traces from curated eval datasets.

Do not persist raw model/tool context “just in case.”
