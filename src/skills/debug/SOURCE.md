---
name: debug
description: >-
  Investigate and fix software failures through evidence, reproduction, boundary tracing, root-
  cause analysis, and focused regression verification. Use for bugs, flaky behavior, CI/test
  failures, unexpected state, or production-like defects. Do not patch by guesswork when the
  failure can be investigated; preserve unrelated working-tree changes and stop once the root
  cause and fix are evidenced.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.0"
---


# Debug

Find the failure mechanism before committing to a fix.

## Workflow

1. Reality-check current code, errors, recent relevant changes, environment/config differences, and working-tree state.
2. Reproduce consistently when possible. For intermittent failures, increase observability or widen the timing/load window without changing the claimed behavior.
3. Trace data/state across the smallest relevant boundaries. In multi-component systems, instrument boundary inputs/outputs to isolate where reality diverges.
4. Form a concrete root-cause hypothesis and seek evidence that could disprove it.
5. Implement the smallest correct fix that addresses the mechanism rather than the symptom.
6. Add or update focused regression evidence and rerun the affected scope.

Do not ask the user to copy facts that logs, source, test output, or repository state can expose directly.

## Outputs

Root cause, evidence, fix, regression evidence, and explicit remaining uncertainty when any exists.

## Stop

Stop when the observed failure is explained by evidence, the fix removes it, and relevant regressions pass. If evidence cannot converge after bounded investigation, report the strongest localization and blocker rather than cycling through speculative patches.
