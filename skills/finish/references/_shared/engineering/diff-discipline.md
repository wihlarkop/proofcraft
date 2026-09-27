# Diff Discipline

Before modifying a repository, inspect the working tree and understand unrelated changes.

- Preserve unrelated user changes.
- Do not reset, clean, or overwrite unrelated files without explicit intent.
- Avoid opportunistic refactors not required for correctness or the requested outcome.
- Include necessary adjacent changes when they are required for correctness, and explain why they are in scope.
- At finish, verify the diff contains only intended or explicitly accepted changes.
