# Reality Check

Before consequential work, reconstruct the state that actually exists.

Start with the current project workspace and its durable artifacts. Treat harness-wide/global/personal memory as non-authoritative project context unless the user explicitly asks to reuse prior context or the workspace itself points to it. If such memory is reused, verify it against current workspace truth before making durable changes.

Inspect only relevant sources, typically:

- current project context, product/spec/ADR/plan artifacts;
- code paths named by the task;
- manifests and migrations where relevant;
- Git branch, HEAD, base, and working tree only when the workspace is actually a Git repository;
- CI/PR status when accessible and material.

Detect capabilities before probing them. “Not a Git repository,” missing manifests, and empty searches are normal evidence in a greenfield workspace, not workflow failures. Avoid bundling expected no-match/unavailable-tool probes into commands whose non-zero exit obscures otherwise successful inspection.

Classify contradictions explicitly. Prefer current workspace code/runtime/configuration evidence over stale plans or conversational assumptions. Preserve unrelated changes. Do not ask the human to relay facts that the available environment can directly reveal.

After making a durable decision or artifact change, re-read the affected orientation/canonical artifacts and remove direct contradictions. Reconcile by updating a stale summary or pointer, not by duplicating the full source of truth.
