# Phone Masking Disabled

This build disables phone-number masking in profile extraction and reports.

Changes:
- `contact_signals.phones_raw` now stores extracted public/self-published phone values.
- `contact_signals.phones_masked` is kept for backward compatibility but now contains the full phone value.
- HTML reports display full phone numbers instead of `+***1234`.

Use full contact values only when lawful, public/self-published, and case-relevant.
