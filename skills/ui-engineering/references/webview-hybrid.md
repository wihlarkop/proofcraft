# WebView / Hybrid UI Boundary

For a WebView or hybrid screen, explicitly assign ownership for:
- navigation and back behavior;
- authentication/session/cookies;
- native-to-web and web-to-native messages;
- serialization/versioning of bridge contracts;
- storage;
- deep links;
- permissions and device capabilities;
- error propagation;
- offline/loading states;
- analytics/telemetry boundaries.

Treat the bridge as an interface contract. Avoid hidden global calls or implicit assumptions that native and web lifecycle events occur together.
