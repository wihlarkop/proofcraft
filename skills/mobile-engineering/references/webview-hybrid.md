# Mobile WebView / Hybrid Boundary

Define whether native or web owns:
- authentication/session refresh;
- top-level and in-WebView navigation;
- back behavior;
- deep links;
- permissions/device APIs;
- storage/cookies;
- file upload/download;
- bridge message versioning;
- loading/offline/error states.

Treat bridge input as an external boundary: validate messages, version contracts deliberately, and avoid exposing unrestricted native capabilities to arbitrary web content.
