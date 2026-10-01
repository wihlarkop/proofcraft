# Operational Simplification

Use for bounded behavior-preserving improvement, especially when a cleanup adds or substitutes concepts.

Prefer delete -> consolidate -> language/framework-native mechanism -> existing owner -> new abstraction. Deviate when project evidence supports a better result. A new abstraction needs multiple real callers/concerns, a required external boundary, materially clearer ownership, or another concrete benefit that outweighs its added concept. A single ordinary caller is insufficient by itself.

## Net complexity check

Compare only the dimensions relevant to the change, before and after; a short explanation is enough, not a scorecard or new artifact:

- concepts and ownership locations;
- wrappers/adapters and execution/composition hops;
- configuration sources and duplicated representations;
- persistent intermediate artifacts and their real consumers.

Question a cleanup when one wrapper merely becomes another, one settings owner becomes multiple configuration sources, or composition gains a forwarding module with no boundary reason. Check whether existing owners or native mechanisms can remove the indirection instead.

For generated/persisted output, identify the actual consumer and source-control contract. Delete an intermediate artifact when direct consumption suffices and no other consumer requires it; retain it when publishing, compatibility checks, or another evidenced consumer requires it.

After implementation, revisit these dimensions before stopping. Fewer lines are not enough if responsibility is more scattered or representations multiply. Accept an increase only with an explicit compensating benefit; do not manufacture a refactor when the implementation is already clear and proportionate.
