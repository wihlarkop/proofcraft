# Transition Model

Describe migration phases explicitly when more than one deployed/data shape can exist:

1. expand/add compatible capability;
2. deploy code that tolerates old and new state;
3. backfill or move data;
4. reconcile;
5. shift authority/traffic;
6. verify;
7. contract/remove old behavior;
8. deprecate and clean up.

Not every migration needs every phase, but destructive work should not be coupled to an earlier additive step merely for convenience.
