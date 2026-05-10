# Completion Upgrade Notes

This build closes the main gaps identified in the original social-media forensics/OSINT brief while staying within public-source and lawful collection boundaries.

## Implemented upgrades

### 1. Deleted / hidden content recovery via public cache analysis
- Rebuilt `osint_forensics/collectors/deleted_recovery.py`.
- Added Internet Archive CDX lookup, Wayback Availability API lookup, and Memento TimeMap lookup.
- Added live public-status classification: accessible, unavailable/not found, restricted/gated, or live-check error.
- Added public archived-body recovery for oldest/latest snapshots when enabled.
- Saves archived HTML, extracted text, metadata JSON, SHA-256 hashes, and evidence records.
- Adds text-diff summary between recovered archive bodies.
- Adds a clear assessment label such as `likely_removed_or_unavailable_now_but_archived_publicly`.
- Explicitly documents that it does not bypass private/login/CAPTCHA/restricted data.

### 2. Workflow integration
- `archive_and_extract()` now automatically performs public archive/cache analysis after snapshot + profile extraction.
- CLI `recover` command now supports:
  - `--fetch-snapshots` to download oldest/latest public archive bodies.
  - `--limit` to control archive lookup size.

### 3. Stronger profile extraction
- Added public post/caption text signals from embedded metadata.
- Added hashtags and relationship co-mention signals.
- Added location timeline extraction from visible text, public embedded metadata, `<time>` tags, and public post/caption text.
- Added relationship-signal summary: mentions, hashtags, linked domains, linked platforms, co-mentions.

### 4. Better network graph generation
- Graph now includes archive lookup nodes, archived snapshot nodes, location-signal nodes, hashtag nodes, and co-mention edges.
- Graph distinguishes public archive evidence from direct profile/page snapshots.
- Interactive graph and JSON/GEXF exports include these new relationship types.

### 5. Report upgrades
- HTML report now has an Archive/Cache section.
- Dashboard shows archive snapshot counts and recovered archived-body counts.
- Profile table now includes location signals and relationship signals.
- Report explains that archive/cache hits are public historical records, not private recovery.

## Verification

Validated with the deterministic offline QA suite:

- `verify-all`: 12 / 12 checks passed.
- Smoke test: passed.
- Evidence hash verification: 0 issues in smoke test.

## Expected project completion after this upgrade

Estimated university/MVP completion: **85%–90%**.

Remaining limitations are mostly platform/API limitations rather than missing implementation:
- True private communication history is not collected.
- Login-only/private followers are not bypassed.
- Live social platforms may block public scraping, rate-limit, or require JavaScript.
- Archive recovery depends on whether public web archives captured the URL.
