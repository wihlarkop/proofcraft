# Existing HTTP service

An established Go HTTP/JSON service. Success bodies are plain domain JSON. Errors use `application/problem+json` with `type`, `title`, `status`, and optional safe `detail`/`field_errors`. `type` is a stable URI identity consumed by the client; `title` can be localized. The response status matches HTTP. This contract is coherent and accepted; consumer compatibility must be preserved.

The scenario request supplies the bounded task. This is a read-only rehearsal: propose concrete changes with code sketches; do not edit the fixture or replace its architecture.
