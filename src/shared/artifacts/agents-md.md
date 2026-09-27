# AGENTS.md Guidance

`AGENTS.md` should remain thin. It points agents toward canonical project context and records only durable repository-wide working rules.

Use a managed block when setup owns only part of an existing file:

`<!-- proofcraft:start schema=1 -->`

`<!-- proofcraft:end -->`

Never overwrite human-authored content outside the managed block. Installing or updating the skill suite must not mutate a repository; repository reconciliation occurs only when setup is explicitly run.
