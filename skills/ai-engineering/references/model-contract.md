# Model Contract

Define the model-facing contract independently of provider SDK details.

Specify:
- task/input context;
- output schema or allowed action;
- deterministic validation;
- confidence/abstention or “no evidence” behavior where applicable;
- latency/cost budget;
- context/token limits;
- timeout/rate-limit/provider failure behavior;
- fallback or human escalation.

Prefer explicit structured output when downstream code depends on machine-readable fields.
