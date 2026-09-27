# Migration Compatibility

Evaluate compatibility from each active participant's perspective:
- old code with new state;
- new code with old state;
- old and new consumers together;
- retries/replays during transition;
- rollback/roll-forward after partial progress.

Prefer expand/contract and additive compatibility windows when live versions overlap. Make the point of no return explicit.
