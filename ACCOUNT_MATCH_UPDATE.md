# Account Match Investigation Update

This build adds a one-button public account matching workflow.

## GUI

Use the **Account Match Investigation** section:

1. Enter the active case name.
2. Enter the username to search.
3. Enter the known public reference account URL.
4. Press **START ACCOUNT MATCH INVESTIGATION**.

The tool will automatically:

- Search public profile URL patterns across supported platforms.
- Archive the reference account snapshot.
- Archive public candidate accounts that resolve.
- Extract public profile signals.
- Compare visible text, handles, links, profile image URLs, and platform resolution confidence.
- Produce confidence scores with reasons.
- Generate an account match HTML report, refresh the case report, verify hashes, and export the evidence bundle.

## CLI

```bash
python main.py account-match <username> <reference_url> --case-id demo_case
```

Example:

```bash
python main.py account-match example https://example.com --case-id demo_case
```

## Scope

The feature only processes public URLs and public profile responses. It does not authenticate, bypass private accounts, evade CAPTCHA, scrape restricted content, or assert identity as fact. Scores are investigative likelihoods requiring analyst review.
