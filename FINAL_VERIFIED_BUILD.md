# Final Verified Build Notes

This version focuses on stability and useful reporting.

## Added public profile intelligence fields

The profile extractor now records:

- Public links found on the profile/page
- Social/linked accounts detected from those links
- Mentioned handles
- Bio candidates
- Follower/following/subscriber signals visible in public text
- Location/country/city hints visible in public text
- Date/history hints such as joined/created/since/founded/started
- Contact signals visible in public text

## Stability fixes

- Selenium is optional and disabled by default in GUI.
- Matplotlib uses the `Agg` backend.
- BLAS thread counts are limited.
- Graph layout avoids NumPy/OpenBLAS matrix inversion paths that caused macOS SIGBUS crashes.
- Export hashes are refreshed after the final package is written, so `verify` is green after packaging.

## Smoke test result

Validated with:

```bash
python main.py smoke-test --case-id smoke_fixed
```

Expected result: `passed: true`, `issues: 0`.
