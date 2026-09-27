# Greenfield Setup

A greenfield project may be an empty ordinary folder or a Git repository. Detect that distinction before running Git-specific checks; source control is optional unless the user or existing workspace establishes it.

Installed agent tooling such as `.agents/` and a skills lockfile does not by itself make the workspace an existing application.

Initialize navigation rather than pretending architecture already exists. Record known facts, create a thin AGENTS managed block and project-context location, establish an ADR convention when useful, and leave stack/provider/architecture choices undecided until shaping or architecture work actually selects them.

Treat expected absence as information. Empty file searches, missing manifests, and “not a Git repository” should be handled as normal greenfield evidence rather than surfaced as failed setup steps.
