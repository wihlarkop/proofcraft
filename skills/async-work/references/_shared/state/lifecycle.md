# State Lifecycle

For meaningful lifecycle behavior, make states and transitions explicit.

Capture only what matters:
- initial state;
- valid events/transitions;
- invalid or duplicate transitions;
- terminal states;
- persistence point;
- cancellation/interruption;
- process restart behavior;
- recovery/reconciliation.

A state machine is a tool, not a requirement. Use one when lifecycle rules are easier to verify as explicit transitions than as scattered conditionals.
