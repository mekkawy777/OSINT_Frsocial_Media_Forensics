# Clean Accurate Fix

This build fixes the report quality issues from the previous accurate build:

- Removed noisy check-only rows from the main report.
- 404, login-gated, JS-gated, and verification pages are hidden as non-findings.
- Supplied public profile URLs are shown as confirmed case targets.
- Extracted account links are grouped as confirmed/extracted account links.
- Generic policy/login/CDN/noisy links are filtered.
- Large link dumps are capped per host to keep the report readable.
- The unified START workflow no longer generates an intermediate report before account matching.
- Timeline metadata is collapsed into clean summary rows instead of huge raw headers.
- Phone detection is stricter to reduce false positives from years, tracking IDs, and page counters.

Run:

```bash
python main.py smoke-test --case-id smoke_test
python main.py --gui
```

Final report:

```text
data/<case_id>/reports/report_latest.html
```
