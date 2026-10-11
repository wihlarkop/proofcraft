# Runtime Workspace

Use this convention for local execution files when a workflow has a concrete reason to retain them. It is a location and lifecycle convention, not a runtime manager or project-knowledge store.

```text
.proofcraft/
  runs/<workflow>/<run-id>/
    run.json
    report.md
    evidence/
    artifacts/
    scratch/
  state/
  cache/
  tmp/
```

Create only the directories a real invocation needs. A run may contain only `run.json`, or selected evidence and artifacts; `report.md` and the per-run subdirectories are optional.

## Ownership and meaning

- `runs/` retains invocation-scoped execution evidence: observations, reports, traces, results, or measurements that explain a particular execution. Evidence supports a judgment; it does not become durable project truth.
- `state/` holds persistent local tool state between invocations. It is not project knowledge or an evidence ledger.
- `cache/` holds reproducible data whose loss is safe because an authoritative source and rebuild path exist.
- `tmp/` holds disposable trusted local intermediates. `scratch/` is disposable work local to one retained run.
- `evidence/` contains direct observations supporting a conclusion. `artifacts/` contains retained supporting files.

Keep project facts in their established canonical owners: project context and `AGENTS.md`, product/spec/design artifacts, ADRs, plans, acceptance records, and handoffs. Do not create `.proofcraft/memory/`, `decisions/`, or `context/`. `.agents/` remains reserved for agent instruction and discovery files.

## Choosing a destination

For an existing project, inspect its established QA, test-output, debug, artifact, and runtime conventions first. Reuse a coherent existing location. Installing or upgrading Proofcraft does not authorize migration or a new `.proofcraft/` layout. Ordinary acceptance, investigation-only debugging, and read-only review do not edit `.gitignore` to create a destination.

Greenfield setup may establish `.proofcraft/` and an ignore rule when workspace establishment is authorized. Preserve existing ignore content. Git is optional. If no safe ignored project-local location exists, use an external temporary location where suitable and report the limitation; do not silently create unignored evidence.

Do not require a run directory for routine work when evidence can be reported directly. Review artifacts are retained only when useful and explicit. Finish consumes current evidence and summarizes it in the canonical handoff/readiness owner instead of copying a second evidence ledger.

## Run metadata and lifecycle

When a run has structured metadata, keep it small: a portable unique run ID, workflow, creation/start time, optional source identity, relevant scope, lifecycle status, and an optional incomplete/blocking reason. Allocate a new run directory exclusively; never overwrite another invocation's directory.

Lifecycle status describes execution (`running`, `completed`, or `incomplete`), not acceptance. A completed execution may have a FAIL, BLOCKED, or NOT RUN verdict. Keep that verdict in the workflow report or acceptance artifact when one is required.

## Safety and retention

Treat runtime files as potentially sensitive. Retain only the observations needed to support the result; avoid secrets, credentials, tokens, personal data, and unnecessary production payloads. Do not stage or commit runtime output automatically. Preserve prior runs by default; delete them only through an explicit cleanup request or an adopted retention policy. Do not follow linked runtime locations or recursively remove unknown directories. Preserve the original filesystem error when a location is inaccessible.

`.proofcraft/` is not a sandbox. It provides no OS-level isolation, resource limits, or artifact-promotion controls. Keep untrusted model/target execution in its separately verified boundary; retain only trusted control-side evidence here. High-assurance security work may require stronger isolation and explicit artifact promotion.
