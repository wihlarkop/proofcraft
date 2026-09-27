# AGENTS.md Guidance

`AGENTS.md` should remain thin. It points agents toward canonical project context and records only durable workspace-wide working rules that must apply before a task-specific skill is loaded.

Use a managed block when setup owns only part of an existing file:

`<!-- proofcraft:start schema=1 -->`

`<!-- proofcraft:end -->`

The managed block should include only bootstrap rules that materially prevent context contamination or unsafe assumptions. Unless an existing project already has equivalent guidance, include:

- Treat files and durable artifacts in the current project workspace as authoritative project context.
- Do not consult harness-wide, global, or personal memory for project facts unless the user explicitly asks to reuse prior context or a project-local artifact points to it. Verify any reused memory against current workspace truth.
- Source control is optional. Do not run Git commands until project-local evidence establishes that the current workspace is inside a Git repository; a non-Git workspace is normal.
- Preserve unrelated user work and follow canonical project artifacts rather than duplicating their contents here.

Keep product, architecture, package versions, commands, and other evolving facts in their canonical artifacts rather than copying them into AGENTS.md.

Never overwrite human-authored content outside the managed block. Installing or updating the skill suite must not mutate a repository; repository reconciliation occurs only when setup is explicitly run.
