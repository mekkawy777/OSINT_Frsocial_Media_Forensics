# University Production Rebuild

This build is the clean one-button rebuild for a university OSINT/social-media forensics project.

## What START does

1. Normalizes and deduplicates the targets.
2. Collects public pages only.
3. Extracts readable profile data: bio/about text, handles, public links, linked accounts, image URLs, follower/count signals, date hints, location/country hints, and contact signals with full phone values.
4. Follows public account/profile links posted inside the collected page or bio, with a strict one-hop limit.
5. Runs username discovery and keeps all outcomes separated into confirmed, possible lead, and not found/unverified.
6. Adds public web-search leads and optional Sherlock/Maigret integration if those tools are already installed locally.
7. Generates a graph, final HTML/Markdown report, evidence manifest, CSV inventory, ZIP bundle, hashes, and audit trail.

## Access boundary

The tool does not bypass logins, CAPTCHA, private profiles, or platform security controls. Blocked or JS-gated pages are reported as possible leads for manual review instead of being misrepresented as confirmed findings.

## Final report

The main report is always:

```text
data/<case_id>/reports/report_latest.html
```

It is designed for non-technical readers and uses these sections:

- Executive Dashboard
- Plain-English Result Guide
- Target Inventory
- Important Account / Page Links
- Collected Public Profile Data
- Account Matching Signals
- Username Search Results
- Public Web Search Leads
- Useful Extracted Links
- Network Graph
- Evidence Inventory
- Timeline
- Audit Trail

## Verification

Run:

```bash
python main.py verify-all
python main.py smoke-test --case-id university_test
```

Expected result: all QA checks pass and hash verification reports zero issues.
