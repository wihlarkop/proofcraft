# Security and Privacy v0.1 Dogfood Evidence

Status: completed representative dogfood for the Proofcraft v0.1 release-candidate assessment.

This record captures a disposable greenfield support-report exercise used to materially validate `security-engineering` and `privacy-engineering`. It is evidence about Proofcraft behavior, not product roadmap.

## Scenario

A signed-in user can submit a support report containing required free text, optional contact email and URL, application version/platform, and a bounded diagnostic excerpt. Authorized support staff can view reports for support work.

The exercise intentionally required:

- server-side ownership and authorization boundaries;
- untrusted free text and URLs;
- diagnostic minimization and secret exclusion;
- purpose limitation;
- unresolved retention, deletion, consent/revocation, residency, user-rights, staff-governance, audit-retention, and incident-response policy;
- provider neutrality;
- no implementation.

## Valid dogfood run

Proofcraft was installed project-locally and the run used:

- core: `setup` -> `shape` -> `architect`, one owner at a time;
- domain: `security-engineering` and `privacy-engineering`.

The run established the following security behavior without selecting vendors:

- report ownership derives from trusted signed-in context rather than client-supplied identity;
- support reads require authorization at the authoritative report boundary;
- client/UI visibility and report identifiers do not grant access;
- free text and URLs remain untrusted and inert, with no automatic URL fetch;
- diagnostics are bounded and exclude unrelated content, secrets, tokens, cookies, authorization headers, and credentials.

The run established the following privacy behavior:

- collection has an explicit support purpose;
- optional email and URL remain optional;
- automatic metadata is bounded to the named support data;
- report data remains purpose-limited across storage, access, copies, logs, and telemetry;
- no unrelated analytics or secondary-use logging was introduced;
- unresolved retention/deletion, diagnostic notice/preview/opt-out/revocation, residency/legal policy, user rights, staff-governance, audit-retention, and incident-response choices remained explicit human decisions.

## Dogfood-derived hardening

The first valid run exposed a readiness-semantics gap: logical architecture was described as settled enough for implementation planning even though material privacy lifecycle decisions were still open.

Proofcraft was hardened in commit `1cb93b3` (`fix: gate unresolved privacy lifecycle policy`):

- `privacy-engineering` now distinguishes architecture readiness from executable implementation-contract readiness;
- unresolved material lifecycle policy is reported to the active core owner as an explicit planning gate;
- placeholder privacy defaults remain prohibited;
- a regression eval covers unresolved lifecycle readiness.

A fresh rerun after that hardening passed:

- the provider-neutral logical boundary remained accepted;
- the spec status was corrected to state that a complete implementation plan is gated by unresolved material human decisions;
- no retention, deletion, consent/revocation, residency, staff-role, audit-retention, legal, or incident-response policy was invented;
- no provider was selected;
- no application code was implemented.

## Excluded attempt

An earlier disposable-workspace attempt is not counted as Proofcraft domain evidence because Proofcraft was not installed in that workspace and unrelated global workflow skills were used instead.

## Release-assessment interpretation

For v0.1 release-candidate assessment:

- `security-engineering` has representative material dogfood for trust boundaries, authorization, secrets exclusion, and untrusted input;
- `privacy-engineering` has representative material dogfood for purpose, minimization, lifecycle-policy gates, and separation from security mechanisms;
- this exercise does not claim implementation/runtime validation of encryption, authentication providers, deletion propagation, retention jobs, auditing, or jurisdiction-specific compliance;
- synthetic eval fixtures remain distinct from this material dogfood evidence.
