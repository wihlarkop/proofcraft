# Architecture Boundaries

Reason about boundaries using ownership and change pressure rather than fashionable topology.

Make explicit:
- policy/business-rule ownership;
- data authority and invariants;
- runtime/process boundaries;
- dependency direction;
- team/operational ownership when relevant;
- compatibility and evolution seams.

A service split, repository abstraction, event bus, or new layer is a hypothesis, not a default. Prefer the simplest boundary that preserves the required invariants and evolution path.
