# Final UI Cleanup Release

This build focuses on user experience, input clarity, case isolation, and a polished dark interface.

## What changed

- Reduced the GUI to four main sections: Overview, Targets & Collect, Analyze & Report, and Evidence.
- Removed all Arabic text from the application interface.
- Improved input placeholders, validation, and error messages.
- Added automatic target type detection for URL, domain, and username entries.
- Kept Active Case as the single source of truth to prevent case mixing.
- Improved the dark neon styling with clearer contrast, cleaner cards, and more consistent buttons.
- Consolidated quick actions so users do not need to jump across many tabs.
- Kept duplicate prevention and unique evidence review through the existing case store.

## Recommended workflow

1. Open the app.
2. Set the Active Case.
3. Add targets in Targets & Collect.
4. Collect selected or pending targets.
5. Generate graph/report in Analyze & Report.
6. Verify hashes and export the final bundle in Evidence.
