# Retrieval and Tool Use

## Retrieval
Define source authority, freshness, indexing/chunk boundaries, retrieval candidates, reranking, provenance/citation, and behavior when evidence is insufficient. Do not let the model invent missing source facts.

## Tools
Treat tools as capabilities with authority and side effects. Validate arguments, scope permissions, make retries/idempotency explicit for mutations, and require human approval where product/security policy demands it.

The model should not gain more authority merely because a tool exists.
