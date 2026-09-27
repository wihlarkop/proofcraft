# Cancellation, Replay, and Backpressure

Long-running work needs lifecycle semantics:
- cancellation request vs confirmed cancellation;
- safe checkpoint/compensation behavior;
- restart/resume;
- replay source and replay safety;
- poison-work quarantine/dead-letter behavior where useful;
- producer throttling, bounded queues, admission control, or load shedding when overloaded.

Do not let queues grow without bound merely to avoid rejecting work; that converts overload into delayed failure.
