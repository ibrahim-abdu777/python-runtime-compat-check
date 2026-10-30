# Python Runtime Fixture

A standard-library-only Python package with a small `unittest` compatibility suite.

Run with:

```sh
python -m unittest discover -v
```

One test sends the documented fixed canary `CANARY-PY-31C8B4`; it never reads files, environment variables, credentials, or standard input.
