# Conflict Resolution

Choose conflict behavior from domain semantics.

Possible approaches include:
- reject stale writes with revision/precondition tokens;
- merge independent fields;
- server authority for selected fields;
- client authority for selected fields;
- explicit user conflict resolution;
- last-write-wins only where losing an intermediate edit is truly acceptable.

State the unit of conflict, timestamps/version source, and what users observe. Avoid silent last-write-wins as a default simply because it is easy.
