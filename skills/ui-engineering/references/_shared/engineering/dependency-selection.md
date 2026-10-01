# Dependency and Toolchain Selection

Prefer the current stack when it can satisfy the requirement cleanly.

## Currentness

When selecting a new runtime, framework, package manager, build tool, or dependency:

- inspect project-local version files, manifests, lockfiles, and accepted architecture first;
- when the user asks for current/latest technology, or the choice depends on current support, verify the stable channel and support status from current primary documentation or the official package/runtime source when available rather than relying on model memory;
- prefer the latest stable **supported and compatible** release, not merely the numerically newest release;
- prefer an LTS/stable channel when its support horizon materially fits the project better than a newer short-lived release;
- avoid alpha, beta, RC, nightly, canary, or other pre-release channels unless explicitly required;
- record an exact reproducible baseline in the project's normal manifest/lock/version mechanism when implementation begins.

Modern tools such as `uv`, Bun, Deno, or newer package/runtime managers are first-class candidates when they fit the required capability. Do not reject a tool merely because it is newer, and do not select it merely because it is fashionable.

## Reversibility and ownership

Classify the choice before freezing it:

- a foundational runtime/framework, deployment-coupled runtime, database product, identity boundary, or other choice whose reversal restructures the system is an architecture concern;
- a package manager, formatter, linter, local runner, or similar convention is normally reversible tooling;
- if a nominal tooling choice also commits the project to a runtime or deployment model (for example, a framework that materially requires a specific runtime), evaluate that combined consequence at architecture level.

Prefer tools that can make the project reproducible with minimal host assumptions when this does not distort the architecture. If a selected tool can provision/manage the required runtime safely, do not require a redundant manual runtime installation solely out of habit.

## New dependencies

When a new dependency is justified:

- prefer a maintained stable release compatible with the project;
- enable only necessary features;
- consider security, license, maintenance, transitive weight, ecosystem/support horizon, and operational cost proportional to the task;
- record why the dependency is necessary when the choice is consequential;
- keep one authoritative dependency source and commit the ecosystem's normal lockfile when reproducibility requires it.

Do not add a dependency merely because an agent is more familiar with it.
