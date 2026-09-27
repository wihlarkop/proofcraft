# Execution Gate

Use a gate only when the work is substantial enough for prerequisites to matter.

Typical evidence:

- expected branch/base is known;
- working tree is clean or intentional changes are understood;
- prerequisite milestone/change is actually complete;
- required spec/ADR/migration state is available;
- blocking CI or build state is known when material.

A contradiction is a stop condition only when proceeding would make the work unreliable or unsafe. Small tasks should not inherit a heavyweight gate.
