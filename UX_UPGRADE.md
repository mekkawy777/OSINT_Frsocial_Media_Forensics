# UX and Case Hygiene Upgrade

## What changed

1. **Global Active Case**
   - The top bar controls the active investigation.
   - All collection/report/export tabs sync to the same case ID.
   - This prevents accidental cross-case contamination.

2. **Mandatory organization**
   - Every case uses its own folder:
     - `data/<case_id>/snapshots/`
     - `data/<case_id>/cache/`
     - `data/<case_id>/graphs/`
     - `data/<case_id>/reports/`
     - `data/<case_id>/exports/`
     - `data/<case_id>/notes/`

3. **Duplicate prevention**
   - Exact duplicate evidence is not inserted twice.
   - Re-generated reports and graphs update stable latest files.
   - Evidence bundle ZIP files avoid duplicate entries.

4. **Better GUI experience**
   - Active Case context bar.
   - Case Manager sync.
   - Evidence Locker table with hash verification status.
   - Quick-open buttons after every successful operation.

5. **Cleaner reporting**
   - `report_latest.html` and `report_latest.md` stay current.
   - `network_latest.png/json/gexf` and `network_interactive_latest.html` stay current.
   - Reports use unique records for clean readable results.

## Recommended workflow

1. Set **Active Case**.
2. Archive public URLs.
3. Search usernames.
4. Query public archives.
5. Generate graph.
6. Generate report.
7. Verify hashes in Evidence Locker.
8. Export final evidence bundle.
