# University Final Verification Build

This build is designed for a one-click public OSINT university project.

## What changed

- One START workflow: targets + optional reference URL.
- Results are separated into:
  - Confirmed public findings
  - Possible leads requiring manual review
  - Not found / blocked / unavailable checks
- The report is written for non-technical readers: summary first, then accounts, public profile facts, candidate leads, useful links, graph, evidence, timeline.
- Username search now shows useful candidate leads instead of hiding everything behind login/JS gates.
- 404/not-found links are never promoted as discovered accounts.
- Optional integration with existing external tools if installed on the machine:
  - `sherlock`
  - `maigret`
- Public web-search candidate collection is included as best effort.
- Phone masking is disabled in this build; public/self-published contact data must only be used when lawful and relevant.

## Verified commands

```bash
python main.py verify-all
python main.py smoke-test --case-id university_test
```

Latest local QA result while packaging:

```text
QA suite: PASSED
Checks: 10 / 10
Smoke pipeline: PASSED
Hash integrity: PASSED
Report generation: PASSED
Graph generation: PASSED
Export bundle: PASSED
```

## Important boundary

The tool does not bypass login, CAPTCHA, private accounts, paywalls, or platform access controls. It collects everything lawfully available from public pages and records blocked/gated pages as possible leads or limitations.
