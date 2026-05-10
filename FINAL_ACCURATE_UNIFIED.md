# Final Accurate Unified Edition

This build addresses the reported problems:

- No 404 links are shown as discovered accounts. Generated platform URLs are stored only as `checked_url`; result buttons appear only for verified public responses.
- Account matching is no longer a separate mental workflow. The app has one **START** flow. Add targets and optionally add a reference URL; the same final report includes collection, profile signals, username search, account matching, graph, evidence, and exports.
- Screenshots are tied to the exact collected URL and are only created when browser collection is explicitly enabled. HTTP-only collection does not create random screenshots.
- Reports use the same black/orange style and are reorganized into clear sections: dashboard, scope, targets, structured profile findings, account matching, username search, links, graph, evidence, timeline, audit.
- Profile extraction now includes useful public signals: bio/description, linked accounts, public links, handles, location/country hints, date/history hints, follower signals, contact signal counts with full phone values, and image/profile-preview URLs.
- Phone masking is disabled in this build; use public/self-published contact data only when lawfully case-relevant.

Run:

```bash
python main.py --gui
```

CLI unified investigation:

```bash
python main.py --no-selenium start https://example.com example --reference-url https://example.com --case-id test_case
```

Smoke test:

```bash
python main.py smoke-test --case-id smoke_test
```
