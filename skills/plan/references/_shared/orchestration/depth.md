# Depth Classification

Use the smallest depth that can safely produce the required outcome.

## Direct
Localized, reversible, well-understood. No formal spec or plan is required.

## Bounded
Scope is clear but there are multiple implementation steps or relevant edge cases. A compact plan is useful.

## Substantial
Cross-module work, persistent state, compatibility, migration, multiple lifecycle states, or consequential architecture. Use a durable plan and acceptance matrix.

## High-assurance
Triggered by risk rather than size: irreversible mutation, security/authorization boundary, money, high-value production data, distributed consistency guarantee, or large blast radius. Add stronger independent/failure/recovery evidence when useful.

TDD is not implied by any depth level.
