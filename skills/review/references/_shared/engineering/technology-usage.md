# Current Technology Usage

Use a selected language, runtime, framework, library, database, build tool, or developer tool through the current supported idioms of the version the project actually uses.

## Inspect first

- Read project-local manifests, lockfiles, version files, configuration, accepted architecture, and nearby working patterns before choosing a usage pattern.
- Prefer an established project convention when it remains supported and fits the accepted architecture.
- When correct usage is version-sensitive, unfamiliar, or materially changed across releases, consult current primary documentation, migration guidance, or maintainer examples for the selected version instead of relying on remembered examples.
- Research only the capability being used; do not turn implementation into a broad documentation survey.

## Implement idiomatically

- Prefer current supported APIs and configuration over deprecated APIs, legacy compatibility shims, or patterns retained only from older versions.
- Respect the technology's intended ownership boundaries instead of reproducing habits from another ecosystem.
- Use the selected package manager, formatter, linter, type checker, migration tool, and build tool through their normal supported workflows rather than emulating a different tool.
- If the project explicitly chose pre-stable or experimental tooling, honor that decision, follow its current documented workflow, and account for known limitations rather than silently replacing it.

## Avoid cargo-cult best practices

- A recommendation is not a requirement merely because it is popular or appears in a template.
- Do not introduce repositories, service layers, factories, dependency-injection frameworks, event buses, caches, wrappers, or other abstraction layers without a concrete project problem they solve.
- Do not rewrite clear working code solely to match a stylistic preference or generic checklist.
- Existing architecture and project-local conventions outrank generic examples unless they are incompatible, deprecated, insecure, or directly contradicted by accepted project truth.

## Verify

Use the cheapest strong evidence appropriate to the changed technology surface: static diagnostics, build checks, focused runtime checks, integration evidence, or observable acceptance behavior. Verification is required; a particular test style is not.
