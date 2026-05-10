# Account Match Bugfix

Fixed a crash in Account Match mode where profile signals (`linked_accounts`, `locations`, and `dates`) were referenced before initialization.

## Fixed error

```text
NameError: name 'linked_accounts' is not defined
```

## Validation

The package was tested with:

```bash
python main.py smoke-test --case-id smoke_fixed
python main.py account-match example https://example.com --case-id match_fixed
```

Both commands completed and generated `report_latest.html` with hash verification passing.
