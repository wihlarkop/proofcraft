# State Authority

Classify state before choosing storage or synchronization behavior.

Ask:
- What state is authoritative?
- What is derived and safely rebuildable?
- What is ephemeral UI/process state?
- What is coordination state whose loss changes correctness?
- What is truly a cache whose loss is safe?

Do not call a dependency a cache merely because it is fast or in-memory. If losing it changes business correctness, treat it as durable or coordination state and design recovery explicitly.
