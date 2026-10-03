---
name: ui-engineering
description: >-
  Design, implement, refine, or review user interfaces across web, desktop, mobile surfaces, and
  hybrid/WebView boundaries. Use for responsive/adaptive layout, interaction behavior, keyboard/
  pointer/touch input, accessibility, visual hierarchy, UX copy, and durable design-system work.
  Preserve project design truth and use optional visual-design providers only when they match the
  current concern; provider availability never overrides DESIGN.md or product behavior.
license: MIT
compatibility: Portable Agent Skills methodology; no runtime dependency.
metadata:
  suite: proofcraft
  suite-version: "0.1.0"
  skill-version: "0.1.3"
---


# UI Engineering

Treat UI as product behavior plus surface engineering, not decoration.

## Trigger

Use for UI layout, interaction, responsive/adaptive behavior, accessibility, visual refinement, UX copy, or surface-specific behavior on web, desktop, mobile, or hybrid/WebView products.

Do not trigger for mobile lifecycle/background/offline behavior without a UI concern; that belongs to mobile-engineering.

## Workflow

1. Inspect current product behavior, existing components/tokens, DESIGN.md, platform targets, and the actual surface before inventing a new visual language.
2. Classify the surface: web, desktop, mobile, or hybrid/WebView. A task may span more than one.
3. Identify the primary UI concern: structure/layout, typography, color, interaction, input modality, motion, accessibility, responsive/adaptive behavior, UX copy, or visual polish.
4. Preserve established design/system patterns unless the task intentionally changes them. When the project has no settled component/styling strategy or the task intentionally revisits it, follow `references/_shared/ui/component-styling-strategy.md` and compare credible strategy shapes from product/design forces before selecting packages.
5. Make behavior work across relevant viewport/window sizes and input modes rather than optimizing a single screenshot.
6. Use motion sparingly and purposefully; respect reduced-motion and accessibility needs.
7. When a specialist visual-design provider is available, route only the matching concern to it and keep project DESIGN.md authoritative.
8. For interactive claims, use `references/_shared/ui/runtime-verification.md` to verify the rendered surface and relevant interactions, viewport/input modes, and state transitions. Type checks, lint, and builds prove static properties, not runtime interaction correctness. Consider SSR/hydration only where present and material. For verification-only requests, report mismatches and the smallest needed fix; change implementation only when repair is explicitly authorized.
9. For visual refinement, inspect the actual rendered surface when available and apply the reference's product-specific visual self-critique. If rendering/runtime access is unavailable, disclose the evidence gap and limit completion claims.

## Component and styling decisions

UI implementation strategy is not automatically an implementation detail. If a component-system, headless-primitives foundation, or styling convention would pervasively structure the frontend and be costly to reverse, report an architecture concern so `architect` can own the durable decision. Otherwise select the smallest suitable strategy here and leave exact reversible tooling to planning/implementation as appropriate.

## Durable design

Update DESIGN.md only when a change establishes durable visual or interaction truth. One-off spacing fixes belong in code, not permanent design documentation.

## Composition

Mobile-specific lifecycle, offline/local-first, backgrounding, device capabilities, or native-shell behavior should add a mobile-engineering concern. Complex WebView bridges may also require API/integration/security concerns.

## Stop

Stop when the requested behavior or specification has sufficient evidence for its claim across relevant surfaces/input modes, with accessibility handled proportionally. Report unavailable rendered/runtime evidence as a remaining gap.
