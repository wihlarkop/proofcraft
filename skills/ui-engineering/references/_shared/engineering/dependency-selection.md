# Dependency Selection

Prefer the current stack when it can satisfy the requirement cleanly.

When a new dependency is justified:

- prefer a maintained stable release compatible with the project;
- avoid alpha/beta/pre-release versions unless explicitly required;
- enable only necessary features;
- consider security, license, maintenance, transitive weight, and operational cost proportional to the task;
- record why the dependency is necessary when the choice is consequential.

Do not add a dependency merely because an agent is more familiar with it.
