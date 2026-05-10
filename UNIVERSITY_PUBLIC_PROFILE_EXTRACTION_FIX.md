# University Public Profile Extraction Fix

This build improves the one-button public OSINT investigation for university demos and reports.

## Fixed

- Extracts bio links from public social profile metadata and embedded page JSON, not only visible `<a>` tags.
- Extracts public business contact signals from `mailto:`, `tel:`, WhatsApp links, and social metadata fields.
- Masks emails and phone numbers in the final report by default.
- Follows one-hop public account links such as Instagram bio links, Linktree/Beacons/Solo.to, YouTube, TikTok, Threads, WhatsApp, Telegram, and common social profile URLs.
- Browser render is enabled by default in the GUI and falls back to normal requests if Chrome/Selenium is unavailable.
- Report now has a dedicated Contact & Business Signals section and clearer Account Links inside profile data.
- Adds deterministic QA check: `embedded_profile_bio_links_contacts`.

## Scope

Public OSINT only. No private-account access, login bypass, CAPTCHA bypass, or hidden-content extraction.
