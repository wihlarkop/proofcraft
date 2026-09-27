---
name: accept
description: >-
  Verify software behavior against observable acceptance criteria using risk-appropriate evidence.
  Use for manual acceptance, integration/contract/E2E checks, regression strategy, exploratory
  checks, or an explicit test-focused request. Render PASS/FAIL/BLOCKED/NOT RUN from direct
  evidence. TDD is available as an optional technique, not the default acceptance workflow.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Accept

Prove product behavior rather than merely running a test command.

## Workflow

1. Identify the behavior/spec/acceptance criteria being claimed.
2. Convert each material criterion into an observable pass/fail condition.
3. Choose evidence by risk: unit, integration, contract, E2E, rendered UI, manual/device interaction, exploratory testing, or a combination.
4. Collect evidence directly when the environment exposes it.
5. Report PASS, FAIL, BLOCKED, or NOT RUN. Missing evidence is not PASS.
6. On failure, record the exact observed mismatch. After a fix, rerun the failed scenario and the affected regression subset.

## Test strategy

Tests should protect behavior and failure modes at the level that can actually falsify the claim. Do not require every behavior to have every test level.

TDD may be used when explicitly requested, required by repository convention, or deliberately selected because test-first discovery helps the task. It is not implied by this skill.

## Stop

Stop when every required criterion has an evidence-backed verdict and remaining gaps are explicit.
