# Test Environment Isolation

Apply when integration/E2E/runtime verification or its setup can mutate a database, service, or other external state. Pure in-memory/static checks do not need this gate.

Before migrations, setup, or write tests:

1. Identify the intended isolated target and permissible test side effects. A dedicated local database, disposable database/branch, container, or equivalent test environment is valid; automatic provisioning is not required. Do not use the normal development target by default. Without an isolated target suitable for the writes, stop and report the missing prerequisite.
2. Resolve the effective migration/setup target, application runtime target, and test endpoint/target independently. Inspect configuration precedence, env-file loading, shell/process overrides, and runner configuration; do not assume env inheritance aligns them. Confirm they refer to the same intended test environment (possibly through different endpoints), not merely similarly named variables.
3. Establish which runtime the runner actually reaches. Existing-server reuse can silently select a development process; disable reuse or verify that process's identity/configuration. A configured launch environment does not prove the reused process has it.
4. Keep server credentials out of client/public frontend configuration and logs. Record sanitized target identity and verification evidence, not full credential-bearing URLs.

For accumulating or destructive writes, establish disposable state or bounded cleanup/reset appropriate to the run. If targets diverge or identity is uncertain, do not run and do not claim E2E acceptance from a prior green result. Resolve the target first, then collect evidence against that runtime. This is a verification gate, not a deployment or database-provisioning workflow.
