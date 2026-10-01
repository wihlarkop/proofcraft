# UI Runtime Verification

Use for interactive behavior claims or visual refinement. Choose evidence that can falsify the specific UI claim:

- **Static:** type checks, lint, and builds establish source/build properties.
- **Runtime/rendered:** the actual surface, interaction, browser/device behavior, and relevant viewport/input mode establish what users see and can do. Use screenshots, traces, or DOM evidence where useful; a screenshot alone does not prove an interaction.

Inspect and exercise the changed surface directly when available. For visual refinement, rendered inspection is required when the environment supports it. If it does not, report the visual/interaction evidence gap; static success cannot substitute for runtime correctness.

## State transitions

When SSR/hydration exists and affects the interaction, inspect initial SSR state and hydrated state separately. Can an enabled control be used before its handler activates? Can hydration restore an SSR default after an early edit? Can a form issue a native submission before the client handler intercepts it? Exercise the relevant timing boundary; do not infer readiness from visible controls alone. Do not impose hydration analysis on non-SSR applications.

When refreshed server data meets local editable state, exercise focus refresh, incoming revisions, and an existing draft. Inspect what is displayed and submitted. Server conflict protection does not prove the editor uses current state; blindly replacing a draft can lose user work. Preserve project-defined draft/reconciliation behavior and report unresolved product choices to the core owner.

## Visual self-critique

Judge the rendered surface against product purpose and established design truth:

- Is information hierarchy clear, and do primary actions compete?
- Do cards/panels group meaningful content or flatten almost every section into equal emphasis?
- Do eyebrow/meta labels and repetitive decoration aid scanning or make the page look generated?
- Does explanatory copy support the task or compete with its content?
- Does hierarchy and interaction hold on relevant mobile/responsive sizes and input modes?

Keep useful structure and styling; no single aesthetic is universally correct. Refine observed weaknesses, then inspect the result and exercise affected interactions.
