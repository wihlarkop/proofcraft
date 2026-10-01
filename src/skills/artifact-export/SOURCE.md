---
name: artifact-export
description: >-
  Export authoritative Proofcraft artifacts into external collaboration formats without replacing
  project truth. Use when the user explicitly asks to transform or share specs, product decisions,
  architecture, or plans in a target format such as OpenSpec. Inspect existing target structure,
  preserve its conventions, never invent missing decisions, and keep exported files derived unless
  the project explicitly adopts the target format as authority.
license: MIT
compatibility: Portable Agent Skills methodology; no mandatory runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Artifact Export

Transform settled Proofcraft knowledge into a requested collaboration format without rerunning product discovery, architecture, or planning.

## Trigger

Use only when the user explicitly asks to export, transform, hand off, or represent existing project artifacts in another format.

Do not trigger merely because another specification tool exists in the workspace, and do not make the external format the project source of truth unless the user or repository already says it is.

## Inputs and context

- the requested target format and scope;
- current project-local canonical artifacts such as product truth, specs, ADRs, plans, and acceptance context;
- any existing target-format configuration, capability paths, naming rules, or in-flight change structure;
- the exact destination when the user supplied one.

## Workflow

1. Inspect current project-local artifacts first and identify the canonical source for every fact to be exported. Do not use stale harness/global memory as source material.
2. Inspect an existing target-format workspace before choosing names or paths. Reuse its conventions and exact capability identifiers where applicable.
3. Build a source-to-target mapping. Transformation may reorganize or restate settled knowledge, but must not create new product decisions, architecture decisions, implementation tasks, or acceptance claims.
4. If a requested target artifact cannot be formed truthfully from available sources, report the gap. Do not fill the gap with plausible defaults.
5. Preserve unresolved decisions as unresolved when the target format supports them. Never convert OPEN or HYPOTHESIS material into settled requirements.
6. Preview the intended output mapping before destructive, ambiguous, or overwrite-prone writes. When the user explicitly requests file creation and the destination is clear and non-conflicting, write directly without an extra ritual.
7. Preserve unrelated target files and working-tree changes. Do not overwrite an existing external-format change or capability unless the requested transformation clearly targets it.
8. Validate with the target tool when it is already available and relevant. The target tool is optional: if it is unavailable, perform structural checks that are possible and state that native validation was not run.
9. Keep Proofcraft canonical artifacts unchanged unless the user separately requests a normal Proofcraft update. Exported artifacts are derived by default.

## OpenSpec target

OpenSpec `spec-driven` schema v1 is the first supported adapter. Load `references/openspec.md` when the target is OpenSpec.

The exporter may derive:

- OpenSpec proposal content from settled problem/motivation/change scope when those facts exist;
- OpenSpec delta specs from settled Proofcraft behavioral requirements;
- OpenSpec design content only from settled architecture/design/plan decisions;
- OpenSpec tasks only from an existing implementation plan or equivalent settled task breakdown.

Do not generate empty or invented OpenSpec artifacts merely to complete the default artifact chain.

## Outputs

Report:

- target format and destination;
- source artifacts used;
- files created or proposed;
- source gaps that prevented any target artifact;
- validation run and result, or explicitly that native validation was not run.

## Composition

Artifact export is a utility, not a core workflow owner. It consumes outputs owned by setup/shape/architect/plan/accept/finish and does not recursively rerun those workflows simply to make an export look complete.

## Verification

Verify that exported behavioral requirements preserve meaning, target paths follow the existing target project when present, no unsupported requirement was promoted, and canonical Proofcraft artifacts remain unchanged.

## Stop

Stop when the requested truthful transformation is written or previewed, validation status is clear, and any unmappable gaps are explicit.

## Escalation

If the target format requires a material product, architecture, or planning decision that is not already settled, stop exporting that portion and route the decision back to the owning Proofcraft workflow rather than deciding it here.
