# Mobile Lifecycle and Background Work

Assume foreground continuity is temporary.

For behavior that spans lifecycle boundaries, define:
- what persists before backgrounding/process death;
- who owns work while backgrounded;
- platform time/execution constraints;
- cancellation semantics;
- restart/resume behavior;
- duplicate work prevention;
- progress/state visibility;
- battery/network constraints where material.

Do not promise indefinite background execution on platforms that do not provide it.
