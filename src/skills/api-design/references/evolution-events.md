# Evolution and Async Contracts

Prefer additive compatible changes while multiple consumers exist. State deprecation timelines and the observable evidence that old behavior is no longer used.

For events/webhooks/streams define:
- event identity;
- schema/version;
- ordering scope;
- duplicate delivery expectation;
- replay/gap behavior;
- acknowledgement semantics where part of the contract.

Migration-engineering owns the multi-stage transition when old and new contracts must coexist operationally.
