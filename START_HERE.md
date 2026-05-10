# START HERE

Run the university-ready one-button OSINT tool:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py verify-all
python main.py smoke-test --case-id university_test
python main.py --gui
```

## GUI usage

1. Enter a Case ID.
2. Paste all targets in Targets, one per line: public URLs, domains, usernames, or profile links.
3. Reference URL is optional. Use it when you want account matching signals included in the same report.
4. Press START.
5. Read the final report at `data/<case_id>/reports/report_latest.html`.

Browser screenshots are optional and disabled by default. Enable them only if Chrome/ChromeDriver works on your machine.

## What it will and will not do

It collects public OSINT only. It follows public links posted in profiles/bios, searches username patterns, collects public profile metadata, and organizes all findings. It does not bypass login, CAPTCHA, private accounts, or access controls.

## Professional completion status

Use this command after installation:

```bash
python main.py verify-all --keep-artifacts
```

The upgraded build validates 16/16 checks, including public interaction extraction, private/internal URL rejection, chain-of-custody export, graph community metrics, hash verification, and final report/bundle generation.

Legal scope: public-source OSINT only. No private messages, login bypass, CAPTCHA bypass, or restricted-content recovery is implemented.
