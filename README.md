# DreamX public integration demo

Synthetic sample data for public repository import and Git workflow checks.
No private application source, credentials or user project data is included.

## Greeting demo

`sample.json` contains synthetic demo data. `greet.py` provides `greet(name)`,
which trims surrounding whitespace and returns `Hello, ` followed by the name.
For example, `greet("  Alice  ")` returns `"Hello, Alice"`. Empty or
whitespace-only names raise `ValueError`.

`test_greet.py` covers a normal name, surrounding spaces, empty input and
whitespace-only input using Python's built-in `unittest` module.

Run the tests from this folder:

```sh
python -m unittest -v
```
