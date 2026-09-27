# Security Review

Evidence-first review:
1. identify a suspicious boundary;
2. trace attacker-controlled input to a sensitive sink/action;
3. account for validation, encoding, framework protections, authentication/authorization, and deployment context;
4. reproduce or otherwise validate exploitability when practical;
5. report the smallest accurate finding and remediation.

Avoid scanner-style speculative findings with no reachable path.
