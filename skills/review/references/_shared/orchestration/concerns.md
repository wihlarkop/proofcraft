# Concern Resolution

Classify concerns before selecting specialist skills.

Typical concern owners:

- UI/layout/interaction/accessibility -> ui-engineering
- mobile lifecycle/offline/device -> mobile-engineering
- schema/query/transaction/data model -> database-engineering
- current-to-target transition/coexistence -> migration-engineering
- consumer-facing contract -> api-design
- external-system boundary -> integration-engineering
- jobs/events/concurrency/replay -> async-work
- runtime/infra/network/CI/IaC -> platform-engineering
- failure/observability/recovery -> reliability-engineering
- trust/auth/secrets/untrusted input -> security-engineering
- retention/deletion/consent/data lifecycle -> privacy-engineering
- latency/throughput/resource efficiency -> performance-engineering
- LLM/RAG/tools/evals/model behavior -> ai-engineering

An explicit repository or component vulnerability audit is owned by the security-audit core workflow, which composes security-engineering. Ordinary PR/diff review remains with review; security-sensitive subject matter alone does not trigger a full audit.

Classify concerns as primary, supporting, or incidental. Load primary and materially relevant supporting capabilities; do not load incidental capabilities merely because they could theoretically apply.
