# Question Strategy

Use this reference when `shape` or `shape:discover` needs human product decisions.

Question strategy controls **how the current decision frontier is asked**, not what the workflow is allowed to decide.

## Strategies

- **adaptive** — default. Start narrow while answers can materially reshape the next question; switch to a bounded batch when the major direction is stable and the remaining material questions are mostly independent.
- **single** — ask exactly one highest-impact material decision at a time.
- **batch** — present the currently visible material decision frontier in one bounded set.

An explicit user request for `single` or `batch` overrides the adaptive default. The user may change strategy during the same shaping/discovery conversation.

## Single

Use single when:

- the product or feature direction is still unstable;
- one answer can invalidate or substantially alter later questions;
- a contradiction needs resolution before the remaining frontier is trustworthy;
- the user explicitly prefers step-by-step discussion.

Ask only the highest-impact unresolved human decision. Do not silently answer neighboring decisions.

## Batch

Use batch when:

- the user explicitly asks to move faster, see all remaining questions, or answer in one pass;
- the major product/feature direction is already stable;
- the remaining decisions are sufficiently independent to answer together.

A batch must be **bounded and material**. Do not dump every conceivable future question merely to appear comprehensive.

When useful, organize the batch as:

- **Contradictions** — only if current decisions genuinely conflict.
- **Must decide / blocks the current outcome** — questions required before the current workflow can become ready.
- **Can defer** — material questions that do not block the current outcome.
- **Conditional** — questions that matter only if a named capability or prior choice is included.

For discovery, the blocking boundary is typically readiness for shaping. For normal shape, the blocking boundary is typically readiness for planning/specification.

Do not include:

- questions already answered by project truth or prior decisions;
- framework, database, provider, file-layout, deployment, or other implementation choices unless they are explicitly the product question;
- cosmetic or cheaply reversible detail;
- speculative questions whose answers are not needed for the current product/feature boundary.

## Adaptive

Adaptive should behave like a conversation, not a fixed quota:

1. Use single while uncertainty is high or decisions are strongly dependent.
2. Re-evaluate after each meaningful answer.
3. Once the direction is stable, batch the remaining visible material frontier when that reduces ceremony.
4. If the batch answers reveal a new dependency or contradiction, ask only the smallest necessary follow-up rather than restarting a broad questionnaire.
5. Stop when the active workflow's readiness condition is met.

Do not switch to batch merely because several questions exist. Switch when asking them together will not hide important dependencies.

## Reconcile after answers

After single or batch answers:

1. Record only conclusions logically supported by the user's answers.
2. Preserve unanswered and conditional decisions as open or deferred.
3. Check the answers against prior decisions for contradictions.
4. Recompute the remaining decision frontier.
5. Declare readiness only when blockers are actually resolved.

Question strategy never authorizes creating durable artifacts in discover mode, guessing missing policy, or extending the scope beyond the active workflow.
