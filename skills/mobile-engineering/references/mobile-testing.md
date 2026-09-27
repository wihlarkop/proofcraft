# Mobile Verification

Choose verification from the mobile failure mode.

Examples:
- pure state/business logic -> focused unit tests;
- persistence/sync -> integration tests with restart/retry/duplicate cases;
- lifecycle/background behavior -> emulator/device lifecycle exercise;
- deep links/push -> platform integration evidence;
- adaptive UI/input -> rendered interaction on relevant sizes/input methods;
- release/signing/store behavior -> actual release artifact/toolchain evidence.

A green widget/unit suite does not prove process-death recovery or real platform lifecycle behavior.
