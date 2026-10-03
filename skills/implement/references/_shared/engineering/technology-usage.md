# Current Technology Usage

Use a selected language, runtime, framework, library, database, build tool, or developer tool through the current supported semantics and idioms of the version the project actually uses.

## Inspect first

- Read project-local manifests, lockfiles, version files, configuration, accepted architecture, and nearby working patterns before choosing a usage pattern.
- Prefer an established project convention when it remains supported and fits the accepted architecture.
- When correct usage is version-sensitive, unfamiliar, or materially changed across releases, consult current primary documentation, migration guidance, or maintainer examples for the selected version instead of relying on remembered examples.
- Research only the capability being used; do not turn implementation into a broad documentation survey.

## Honor semantic contracts

- Treat idiomatic usage as more than syntax or style. Choose APIs and constructs according to the actual contract: required versus optional presence, recoverable absence versus invariant failure, owned versus borrowed/resource-scoped lifetime, sync versus async execution, mutable versus immutable state, transaction ownership, and other semantics the technology exposes.
- Prefer the technology's explicit absence/error/state mechanisms when absence, failure, or alternatives are valid runtime states. Conversely, do not use permissive or fallback APIs where a missing value should expose a broken internal invariant.
- When a value obtained through an optional/fallible lookup is required downstream, validate or narrow it explicitly rather than letting an ambiguous null/none/undefined/default value propagate.
- Do not transplant habits from another language or framework when the selected ecosystem has a clearer native mechanism. A pattern that is conventional elsewhere is not automatically good practice here.
- Preserve stable shapes with the project's normal typed/modeling mechanism when that reduces ambiguity; do not replace a clear typed boundary with loose maps/objects merely for convenience, and do not introduce heavyweight modeling for genuinely ad-hoc data.

## Implement idiomatically

- Prefer current supported APIs and configuration over deprecated APIs, legacy compatibility shims, or patterns retained only from older versions.
- Respect the technology's intended ownership, lifecycle, extension, and composition boundaries instead of reproducing habits from another ecosystem.
- Use framework extension points and lifecycle hooks only when they own the behavior; do not wrap native mechanisms merely to make every technology look structurally identical.
- Use the selected package manager, formatter, linter, type checker, migration tool, code generator, and build tool through their normal supported workflows rather than emulating a different tool.
- Respect tool-owned generated artifacts, lockfiles, configuration precedence, cache/state directories, and update workflows instead of bypassing them with manual copies or parallel representations.
- If the project explicitly chose pre-stable or experimental tooling, honor that decision, follow its current documented workflow, and account for known limitations rather than silently replacing it.

## Avoid cargo-cult best practices

- A recommendation is not a requirement merely because it is popular or appears in a template.
- Distinguish correctness/semantic guidance from subjective style. Prefer formatter/linter enforcement for mechanical style and reserve human/agent findings for choices that materially affect clarity, correctness, ownership, compatibility, or maintainability.
- Do not introduce repositories, service layers, factories, dependency-injection frameworks, event buses, caches, wrappers, or other abstraction layers without a concrete project problem they solve.
- Do not rewrite clear working code solely to match a stylistic preference or generic checklist.
- Existing architecture and project-local conventions outrank generic examples unless they are incompatible, deprecated, insecure, or directly contradicted by accepted project truth.

## Verify

Use the cheapest strong evidence appropriate to the changed technology surface: static diagnostics, build checks, focused runtime checks, integration evidence, or observable acceptance behavior. Verification is required; a particular test style is not.
