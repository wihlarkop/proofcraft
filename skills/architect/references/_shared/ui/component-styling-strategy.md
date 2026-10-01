# UI Component and Styling Strategy

Use this when a project must choose how reusable UI behavior and visual styling are implemented across a meaningful surface.

## Separate strategy from package choice

First choose the strategy shape from product and design forces. Exact libraries/packages come later unless the library itself would become a pervasive, hard-to-reverse dependency.

Component strategy candidates may include:

- **custom components** — project-owned primitives and composites;
- **headless/accessibility primitives + custom styling** — reusable interaction behavior without adopting a visual system;
- **styled component system/library** — a third-party visual/component language adopted broadly;
- **hybrid** — custom product components built on selected primitives, with third-party styled components used only where justified.

Styling strategy candidates may include:

- component/scoped CSS;
- CSS Modules or equivalent local scoping;
- utility-first CSS;
- token-driven global styles plus local component styles;
- CSS-in-JS or another runtime styling model when the platform makes it appropriate.

Do not default to Tailwind, shadcn-style components, Material-style systems, Bootstrap, a headless library, or plain CSS merely because they are popular, installed, familiar, or fast for a demo.

## Derive from surface forces

Compare credible strategies against evidence such as:

- how distinctive or branded the product should feel;
- density and complexity of interactive controls;
- keyboard, screen-reader, pointer, and touch requirements;
- responsive/adaptive behavior across target surfaces;
- theming, dark mode, and design-token needs;
- expected amount of custom visual treatment;
- need for complex accessible primitives such as dialogs, menus, comboboxes, popovers, tabs, and data grids;
- SSR/hydration/platform compatibility;
- bundle/runtime cost where material;
- testability and visual-regression needs;
- maintenance burden and upgrade/migration cost;
- whether a design system already exists in DESIGN.md or the repository.

## Ownership and durability

Treat these differently:

- **architecture-level UI strategy** — pervasive decisions whose reversal would restructure most of the frontend, such as adopting a broad styled component system, a utility-first convention across the product, or an application-wide headless-primitives foundation;
- **durable design truth** — tokens, interaction conventions, density, motion, responsive behavior, accessibility expectations, and product-specific component semantics belong in DESIGN.md when established;
- **reversible implementation details** — a small icon package, one-off helper, formatter, or narrowly used component utility generally belongs to plan/implementation rather than an ADR.

When a strategy is architecture-level, `architect` owns the durable decision and `ui-engineering` supplies the surface-specific evidence. When it is not architecture-level, `ui-engineering` may choose it directly within accepted architecture.

## Selection rules

Prefer the smallest strategy that satisfies the product's real UI needs.

- Do not hand-roll complex accessibility behavior merely to avoid dependencies when a maintained primitive library materially reduces risk.
- Do not adopt a large styled system when the product requires a distinctive custom visual language and only a small subset of components.
- Do not adopt a utility framework when ordinary scoped styles and tokens are sufficient, unless the utility convention materially improves the project's maintainability.
- Do not build a custom design system before repeated product patterns justify one.
- If a third-party component library is selected, record what it owns and what remains project-owned so future contributors do not mix visual systems accidentally.

Exact dependencies should follow the shared dependency-selection guidance: maintained stable releases, only necessary features, and no dependency based solely on familiarity.
