# Social Media Forensics & OSINT - Final Accurate Unified Edition

One-button public-source investigation framework. This edition is accuracy-first: it does not show 404/generated URLs as discovered accounts, keeps Account Matching inside the same comprehensive START workflow, and generates one organized black/orange report.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py smoke-test --case-id smoke_test
python main.py --gui
```


## Professional Completion Upgrade

This build adds the missing professional layers requested after the initial MVP review:

- Public-scope URL guardrails: localhost/private/internal/metadata URLs and credential-bearing URLs are rejected.
- Public interaction extraction: mentions, hashtags, public reply/comment/status links, timestamps, and visible reaction counters.
- Stronger network analysis: interaction nodes plus community summaries in graph metrics.
- Chain of custody: `exports/chain_of_custody.json` with deterministic evidence/audit hash chains.
- Report readiness: Forensic Readiness & Scope section, readiness score, scope notice, and chain link.
- Faster offline handling: public archive lookup records `network_unavailable` cleanly when DNS is blocked.

Validation: `python main.py verify-all --keep-artifacts` passes **16/16** deterministic QA checks in an offline environment.

## How to Use

1. Enter a Case ID.
2. Paste targets, one per line: URLs, domains, usernames, or public profiles.
3. Optional: paste a known public reference account URL. When present, username targets are compared against that reference inside the same final report.
4. Click **START**.
5. Open `data/<case_id>/reports/report_latest.html`.

## Important Accuracy Rules

- Platform URL patterns are checked, not blindly reported.
- A link appears as a discovered account only when the public HTTP response validates it.
- 404/login/blocked/check-only URLs remain in raw evidence but are not promoted as findings.
- Screenshots are only produced by explicit browser collection and tied to the collected URL.
- Phone numbers are shown in full in this build; email signals remain masked by default.


---

# Social Media Forensics & OSINT Investigation Framework — Ultimate Edition

A production-oriented public OSINT and forensic evidence collection framework with a polished PySide6 GUI, CLI workflows, network graph analysis, evidence hashing, interactive reports, and investigator-focused exports.

## Responsible-use scope

This framework collects and analyzes **public-source evidence only**. It does not bypass authentication, privacy controls, CAPTCHAs, platform restrictions, or access private/deleted content. Historical recovery is limited to public archive lookups such as Internet Archive metadata and locally preserved snapshots.

## Core features

1. **Social Media Content Archiving** — Preserve public URL snapshots, HTML/text metadata, UTC timestamps, headers, screenshot when Selenium is available, and SHA-256 hashes.
2. **User Profile Extraction** — Extract public profile/page signals: handles, bios, follower/following strings, location hints, canonical URLs, metadata, and links.
3. **Network Graph Generation** — Generate PNG, GEXF, JSON, and a self-contained **interactive HTML graph** with filtering, search, node inspection, colors, and relationship details.
4. **Username Cross-Platform Search** — Check common public profile URL patterns and produce confidence-scored leads.
5. **Historical Recovery** — Query public archive records and preserve lookup evidence.
6. **Social Network Analysis Reports** — Generate polished HTML and Markdown reports with timeline, evidence table, link buttons, confidence summaries, graph metrics, analyst notes, exports, and integrity verification.

## New Ultimate Edition improvements

- **Case Manager** tab for existing investigations.
- **Evidence Locker** tab for hash verification, CSV/manifest/ZIP export, and analyst notes.
- **Interactive network graph** with search, filters, node inspector, link buttons, and type-based colors.
- **Confidence-scored username results** in the report.
- **Clickable investigation links** as cards/buttons.
- **Evidence bundle ZIP** for portable case review.
- **CSV evidence inventory** for spreadsheet workflows.
- **Hash verification workflow** with OK/issue counts.
- **Analyst notes** that appear in the final report.
- **CLI commands** for demo, archive, username search, recovery, graphing, reports, verification, exports, notes, and case listing.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Launch the GUI

```bash
python main.py --gui
```

## Run the complete safe demo

```bash
python main.py --demo --case demo_case
```

## CLI examples

```bash
# Archive and extract a public URL
python main.py archive https://example.com --case-id test_case_01

# Search a username across public platform URL patterns
python main.py username openai --case-id test_case_01

# Query public historical archive records
python main.py recover https://example.com --case-id test_case_01

# Generate graph outputs: PNG, GEXF, JSON, interactive HTML
python main.py graph --case-id test_case_01

# Generate final report and exports
python main.py report --case-id test_case_01

# Verify hashes
python main.py verify --case-id test_case_01

# Export evidence bundle
python main.py export --case-id test_case_01

# Add analyst note
python main.py note "Reviewed GitHub result; looks relevant but needs manual confirmation" --case-id test_case_01 --status "Needs Follow-up"

# List cases
python main.py cases
```

## Output structure

```text
data/<case_id>/
  snapshots/    # preserved page snapshots and profile_extraction.json
  cache/        # username search and archive lookup JSON
  graphs/       # PNG, GEXF, JSON, interactive graph HTML
  reports/      # HTML and Markdown reports
  exports/      # manifest JSON, CSV inventory, evidence bundle ZIP
```

## Reading the report

- **Executive Dashboard**: evidence counts, username hits, and graph relationship totals.
- **Cross-Platform Username Results**: platform, status, confidence bucket, reason, and open button.
- **Investigation Links**: clickable cards for profile/source URLs.
- **Network Graph**: PNG preview plus button to the interactive graph.
- **Exports & Integrity**: manifest, CSV inventory, ZIP bundle, hash verification status.
- **Evidence Inventory**: every stored item with SHA-256 hash and open button.
- **Forensic Timeline**: ordered evidence events with metadata details.

## Notes on Selenium

Selenium improves snapshot fidelity and screenshots. If Selenium or a browser driver is unavailable, use `--no-selenium` or uncheck Selenium in the GUI; the framework will fall back to HTTP collection where appropriate.

## UX + Case Hygiene Upgrade

This build adds mandatory case hygiene and a cleaner investigation experience:

- **Active Case Bar:** one global case context is applied across all tabs so evidence cannot accidentally be written to a different case.
- **Case ID normalization:** case names are converted to safe lowercase slugs, for example `Test Case 01` becomes `test_case_01`.
- **No duplicate evidence rows:** exact duplicate evidence is not inserted again. Stable generated artifacts are updated in place.
- **Stable output names:** repeated graph/report generation now updates `network_latest.*` and `report_latest.*` instead of creating many confusing copies.
- **Evidence Locker table:** the GUI now shows a unique evidence table with hash status, source, timestamp, and path.
- **Cleaner evidence bundles:** ZIP exports avoid duplicate archive entries and include snapshot folders safely.
- **Improved workflow order:** the recommended flow is Active Case → Archive → Username Search → Historical Recovery → Graph → Report → Evidence Locker verification.

These changes are designed to keep each case isolated, reduce clutter, and make the application easier to use during real investigation workflows.

## Dark Aurora