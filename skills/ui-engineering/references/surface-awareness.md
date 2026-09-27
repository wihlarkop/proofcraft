# Surface Awareness

Determine where the UI runs before choosing interaction rules.

## Web
Consider responsive viewport changes, browser navigation, pointer + keyboard + touch, focus, semantics, zoom, and browser constraints.

## Desktop
Consider resizable windows, dense information layout, keyboard shortcuts, hover/context actions, multi-window expectations when relevant, and native desktop conventions.

## Mobile
Consider compact/adaptive layout, safe areas, touch targets, gestures, system back behavior, software keyboard/IME, orientation, and platform navigation conventions. Route lifecycle/offline/background behavior to mobile-engineering.

## Hybrid / WebView
Treat the native shell and web content as separate runtime owners. Make navigation, auth/session, storage, deep links, permissions, bridge calls, errors, and offline ownership explicit.
