# Diff Discipline

Before modifying a repository, inspect the working tree and understand unrelated changes.

- Preserve unrelated user changes.
- Do not reset, clean, or overwrite unrelated files without explicit intent.
- Avoid opportunistic refactors not required for correctness or the requested outcome.
- Include necessary adjacent changes when they are required for correctness, and explain why they are in scope.
- At finish, verify the delivered diff contains only intended or explicitly accepted changes; unrelated working-tree work may legitimately remain.

## Change review and finish hygiene

When Git exists, inspect source-control reality, not just the edited files or a green test result:

1. Use the actual delivery comparison (base-to-change diff for a branch/PR, plus relevant staged/unstaged changes). Check both diff content and newly tracked paths; a working-tree-only diff can miss pollution already committed on the branch.
2. Investigate unexpected file counts or paths: local agent/tool installations, caches, temporary output, test traces/screenshots, generated files without intended source-control ownership, secrets/env files, and local configuration. Count/path anomalies are prompts to inspect purpose and project policy, not automatic findings. Avoid printing secret contents.
3. Inspect untracked paths when they affect the claim: a missing migration or source file matters; unrelated notes and retained local evidence need not be delivered. Do not flag every untracked file or demand a clean tree.
4. Separate intended deliverables from accidental additions and unrelated user work. Respect project ownership of committed generated distributions. In read-only review, recommend scoped remediation. When cleanup is authorized, remove accidental tracking and add an appropriate ignore rule while preserving local installations/files; verify both tracking and local presence afterward. An ignore rule alone does not untrack existing files. Do not delete local skills or use broad clean/reset operations to fix repository pollution.
