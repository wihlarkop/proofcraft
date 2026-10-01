# Recommend Mode

Help the human decide **what to shape next** for an existing product. This is a mode of shape, not a lifecycle stage or an automatic roadmap.

## Routing

Use for requests such as “what feature should we build next?”, “recommend the next product feature”, “what should I add to this app?”, “what opportunities are left?”, or “what would make this product more useful next?” when choosing the next product opportunity is the task. The alias is `recommend` → `shape:recommend`.

An already selected feature, behavior recommendation within that feature, or spec request stays in normal shape/spec. Resuming eligible work in an accepted plan belongs to continue. Engineering recommendations belong to the relevant engineering workflow (for example improve for behavior-preserving cleanup); do not recast refactors as product features. Exploring what product or major direction should exist belongs to discover.

## Evidence before candidates

Use shape's existing reality-check and decision-lock guidance. Inspect relevant repository truth before proposing opportunities:

- product direction, users/jobs, constraints, and product docs;
- behavioral specs and implemented capabilities, with acceptance evidence where available;
- accepted architecture where it affects feasibility or dependencies;
- explicit deferrals and non-goals;
- current plans, handoffs, and backlog when present.

Use concrete artifact/code pointers to support claims. Check stale plans/backlog against current implementation so shipped work is not recommended as missing. An unmet goal or backlog entry supports a possibility, not approval to build it. Existing implementation shows capabilities, not user demand.

If accepted direction or baseline cannot be established, say what is missing and ask only the material product question needed to proceed, using the existing question strategy. When direction itself is undecided, suggest discover. Do not invent a product category from a template, manufacture confidence, or fill a quota with generic ideas.

## Recommendation contract

Identify gaps between the accepted product purpose and current behavior. Offer a small useful set, typically **3–5 candidates**, honoring a requested count or several-options comparison when evidence supports it. Fewer grounded candidates are better than padding. For each, give enough to compare:

- the user/product problem and plausible benefit;
- why it is relevant now, with current repository evidence;
- important dependencies and feasibility constraints;
- material product uncertainty or assumptions;
- rough relative scope/risk when useful, without an implementation plan.

Keep evidence status visible:

- **Supported** — directly grounded in accepted direction, documented gaps, or current behavior. This does not establish demand or priority by itself.
- **Hypothesis** — a plausible inference tied to that evidence; name the unconfirmed assumption and what would resolve it. Do not invent research, demand, telemetry, market evidence, or pain points.
- **Deferred** — explicitly postponed or excluded by current decisions. If surfaced, label the conflict and explain why it is worth considering now and which decision/dependency still blocks it. A candidate may be both supported by product purpose and deferred; do not erase either status or silently reopen the decision.

When evidence favors one candidate, recommend it with comparative reasoning about product value, the implemented foundation, dependencies, and uncertainty. Do not force a winner when the user wants options or the evidence is weak, and do not use arbitrary numeric scoring. Do not turn the set into a long roadmap or select technologies/providers. Surface feasibility constraints without replacing accepted architecture.

External market/competitor research is optional: use it when explicitly requested or when the decision genuinely depends on current external facts. Attribute sources, distinguish observed competitor capabilities from inferred value/demand, and state unavailable evidence honestly. Repository product truth remains the basis; installed browsing/provider capabilities alone do not justify research or adoption.

## Human selection boundary

Return advisory recommendations and the remaining decision, with no durable product/spec/backlog updates, architecture, plan, or code. Urgency or “pick for me and assume it is approved” does not confirm a concrete candidate the human has not yet reviewed. Present the recommendation for selection/confirmation instead.

Once the human selects or confirms a concrete opportunity, transition to normal shape for that candidate. Carry evidence and explicitly open assumptions forward; advisory details are not decided feature behavior. Normal shaping may capture actually settled decisions under its existing artifact rules, then determine the appropriate next stage. Do not rerun opportunity selection or jump directly to planning/implementation merely because a candidate was selected.
