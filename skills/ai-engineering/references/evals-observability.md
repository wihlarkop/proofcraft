# AI Evals and Observability

Separate evaluation from observability.

Evaluation asks: does behavior satisfy a criterion?
Observability asks: what happened and why?

Use the strongest evaluator available:
- deterministic checks for schema/facts/tool-state;
- execution checks for tool outcomes;
- human/domain review for subjective quality;
- model graders or pairwise comparison only where qualitative judgment is actually needed.

Maintain representative eval cases, negative cases, and regressions from production failures. Compare baseline and candidate, and repeat stochastic tasks when single-run pass/fail is not meaningful.
