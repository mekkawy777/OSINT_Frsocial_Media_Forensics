# Final UI and Report Update

This build focuses on a simpler investigation flow and a cleaner final report.

## Changes

- Removed all visible references to the previous scan branding term.
- Main action button is now **START**.
- Inputs are separated clearly:
  - Full Investigation mode uses the **Targets** multi-line box.
  - Account Match mode uses separate **Username** and **Reference** fields.
- The GUI keeps the black/orange dark style and includes a decorative scan animation.
- The final report is a single consolidated `report_latest.html` file.
- The report now uses the same black/orange visual identity as the app.
- Report sections include executive dashboard, methodology, targets, account match results, username results, links, graph, exports, evidence inventory, timeline, analyst notes, and audit trail.

## Start

```bash
python main.py --gui
```
