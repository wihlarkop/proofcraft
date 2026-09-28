# Discover Mode

Use discover only when the user is genuinely exploring what product or major product direction should exist, or explicitly asks for product discovery.

## Trigger

Appropriate triggers include:

- a new software-product idea whose value, users, core job, or scope is still unclear;
- exploration of a major new product direction before deciding to build it;
- an explicit request to discover, explore, or think through the product before shaping it.

Do not activate discover merely because work is greenfield, because a feature has a few unresolved requirements, or because implementation has not started. Ordinary requirement ambiguity belongs to normal shape.

## Conversation contract

1. Start from the current workspace. Treat project-local files and explicitly provided conversation context as authoritative discovery context. Do not inspect harness/global/personal memory (for example Codex memory files) unless the user explicitly asks to reuse it or the workspace itself points there; verify any reused memory against workspace truth before relying on it.
2. Stay conversational first. Do not create code, architecture, plans, specs, `PRODUCT.md`, `AGENTS.md`, or other durable project artifacts by default.
3. Ask one meaningful product question at a time. Ask only when the answer materially changes product behavior, scope, risk, target user/job, or major direction.
4. Challenge weak assumptions, contradictions, and unnecessary complexity instead of simply agreeing.
5. Distinguish conclusions as **DECIDED**, **HYPOTHESIS**, **OPEN**, and **DEFERRED**. Do not promote a hypothesis or implementation idea into product truth.
6. Look for the smallest useful product or coherent first product slice without forcing an artificial MVP ritual.
7. If a material decision depends on an external or technical fact, inspect or research that fact when capabilities allow; otherwise classify it as **NEEDS_RESEARCH** instead of guessing.
8. Existing project artifacts and code may be inspected for facts when discovery happens inside an established product, but existing implementation does not automatically decide new product intent.
9. Do not select language, framework, database, provider, deployment model, or other implementation mechanisms unless the user is explicitly comparing those as the product-level question.
10. Stop asking once product clarity is sufficient. Do not continue into low-impact naming, file-placement, UI-detail, or reversible implementation questions just to prolong discovery.
11. Discovery notes are not a transcript. When thinking converges, summarize conclusions and unresolved decisions only.

## Outcomes

End discover with exactly one readiness outcome when a checkpoint is useful:

- **READY_TO_SHAPE** — product direction is clear enough for normal shaping/specification.
- **NEEDS_MORE_DISCOVERY** — a material product question still needs human exploration.
- **NEEDS_RESEARCH** — a material external/technical uncertainty should be verified before shaping.
- **PARK** — there is not enough value/clarity to continue building now.

`READY_TO_SHAPE` does not itself authorize writing durable artifacts. If the user wants the conclusions captured, transition to normal shape/setup as appropriate and persist only durable conclusions, not the discovery transcript.
