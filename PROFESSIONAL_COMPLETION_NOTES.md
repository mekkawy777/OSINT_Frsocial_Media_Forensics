# Professional Completion Upgrade

This build closes the remaining MVP gaps while keeping the tool legally scoped to **public OSINT evidence only**.

## What was added

### 1. Public-scope guardrails
- Rejects localhost, loopback, link-local, private/internal IPs, cloud metadata IPs, and credential-bearing URLs.
- Adds an explicit public OSINT scope policy to system checks and reports.
- Documents that private messages, login bypass, CAPTCHA bypass, paid/private groups, and non-public follower/friend graphs are not implemented.

### 2. Public interaction extraction
- Extracts public interaction breadcrumbs from visible text, embedded public captions, public status/post/comment/reply links, mentions, hashtags, timestamps, and reaction counters.
- These are stored in `profile_extraction.json` under `public_interactions`.
- They are shown in the HTML report and connected into the network graph.

### 3. Stronger network analysis
- Adds interaction nodes and edges to the graph.
- Adds community summaries to graph metrics for relationship-cluster review.
- Keeps relationship labels explicit: public link, public mention, public co-mention, public hashtag, public archive body, etc.

### 4. Chain of custody
- Exports `exports/chain_of_custody.json`.
- Builds deterministic hash chains over evidence records and audit events.
- Includes the chain file in the evidence ZIP and report export links.

### 5. Better archive/cache handling
- Historical recovery remains limited to public archives/caches.
- When DNS/network is unavailable, the archive collector now records a clean `network_unavailable` result instead of wasting time on repeated failed archive calls.

### 6. Report readiness
- Adds a Forensic Readiness & Scope section.
- Adds readiness score, scope notice, chain-of-custody link, and public interaction counts.

## QA status

`python main.py verify-all --keep-artifacts` now validates 16 checks:

1. Offline demo pipeline
2. Hash integrity
3. Final outputs exist
4. Username 404 accuracy
5. Target dedupe
6. Analyst notes
7. Historical archive demo
8. Report structure/noise filter
9. Public linked-account following
10. Embedded profile links/contacts
11. Public interaction extraction
12. Private URL scope guard
13. Chain-of-custody export
14. Graph community metrics
15. Workflow status/health
16. System doctor

Latest run: **16/16 passed**.

## Important legal/accuracy boundary

The project is now closer to a professional public OSINT framework, but it intentionally does not perform unlawful or restricted actions. It does not read private messages, bypass login/CAPTCHA, scrape private accounts, recover non-public deleted content, or claim identity confirmation from weak public signals. Findings are leads/evidence artifacts that require analyst review.
