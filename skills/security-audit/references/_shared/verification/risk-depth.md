# Risk-Based Verification

Choose the cheapest sufficient evidence for the actual risk.

Possible evidence, not a mandatory sequence:

- formatter/static analysis;
- focused compile/typecheck;
- targeted unit tests;
- affected integration/contract tests;
- build;
- rendered/manual/device acceptance;
- broader regression;
- full suite;
- failure/recovery exercise for high-risk work.

The type of test follows the failure risk. TDD is an optional implementation technique, not a verification requirement.
