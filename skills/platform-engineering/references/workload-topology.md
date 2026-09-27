# Workload and Topology

Map requirements before naming infrastructure.

Clarify:
- request/worker/batch/stream execution model;
- stateful vs stateless boundaries;
- ingress/egress and network trust;
- availability and scaling needs;
- startup/shutdown behavior;
- regional/latency constraints;
- operational ownership;
- cost envelope.

Do not introduce orchestration layers, service meshes, or managed services without a requirement they solve.
