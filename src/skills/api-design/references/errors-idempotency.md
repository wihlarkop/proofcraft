# Errors, Preconditions, and Idempotency

For mutations, make failure behavior machine-usable.

Clarify:
- validation vs authentication/authorization vs conflict vs unavailable;
- stable error codes/details;
- retryable vs permanent failures;
- idempotency-key scope and retention;
- concurrency/version preconditions;
- partial success;
- timeout/unknown-outcome behavior.

Do not tell consumers to “just retry” unless duplicate side effects are safely bounded.
