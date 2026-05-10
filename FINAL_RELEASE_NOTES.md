# Final Release Notes — Pro Investigator Dark Aurora

This is intended as the final polished release of the local public-OSINT investigation framework.

## UX changes

- A unified Active Case Bar prevents accidental writes to the wrong case.
- Target Manager centralizes URLs, usernames, domains, priorities, tags, notes, and collection status.
- Case Manager summarizes existing cases.
- Evidence Locker deduplicates visible records and verifies SHA-256 hashes.
- Quick-open artifact buttons appear after every action.
- Final Package action generates graph, report, verification, CSV, manifest, and bundle in one step.

## Investigation hygiene

- Case IDs are normalized to safe slugs.
- Targets are deduplicated by case/type/value.
- Evidence is deduplicated by case/kind/source/hash.
- Stable report/graph/export filenames keep each case clean.
- Reports include target inventory, guided workflow status, analyst notes, timeline, evidence table, links, graph artifacts, and verification summary.

## Scope

The project is designed for lawful public-source investigation workflows only. It does not bypass authentication, CAPTCHA, privacy controls, rate limits, or restricted content.
