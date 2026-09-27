# Observability

Start with a question, not a telemetry type.

Examples:
- Why did this request fail?
- Which dependency is adding latency?
- How many retries/replays occur?
- Is a backlog growing?
- Did recovery restore user-visible behavior?

Choose the minimum signal that answers the question. Prefer structured, correlated, privacy-conscious telemetry. Remove temporary noisy instrumentation when the investigation ends unless it has durable operational value.
