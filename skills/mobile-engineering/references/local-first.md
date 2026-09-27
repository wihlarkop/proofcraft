# Local-First Mobile Behavior

Use local-first when product value should continue despite unreliable or absent connectivity.

A robust local-first flow normally makes locally accepted work durable before presenting success, assigns stable identities to queued mutations, and treats synchronization as later reconciliation with remote state.

Clarify:
- what works fully offline;
- what requires network;
- what is authoritative while disconnected;
- how long local data remains useful;
- what happens after app/process restart;
- how sync status or conflicts are communicated.

Do not add offline write queues to products whose behavior does not require them.
