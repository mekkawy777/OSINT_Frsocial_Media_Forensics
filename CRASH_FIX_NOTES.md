# Crash Fix Notes

This build fixes a macOS/Apple Silicon crash that could happen while generating a network graph from the GUI worker thread.

Changes:

- Replaced `networkx.spring_layout()` with a deterministic pure-Python component layout.
- Forced Matplotlib to use the `Agg` backend for report/PNG generation.
- Limited BLAS numerical worker threads through environment defaults.
- Increased the GUI worker thread stack size.
- Kept a single final report path: `data/<case_id>/reports/report_latest.html`.

The report keeps the same Black/Orange style as the app and no longer uses the word Radar.
