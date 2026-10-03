# chemeng-toolkit

![tests](https://github.com/aman19-ux/chemeng-toolkit/actions/workflows/tests.yml/badge.svg)

Small, tested Python functions for common chemical engineering calculations.

## Running the tests

```
python -m venv .venv
.venv\Scripts\python -m pip install pytest
.venv\Scripts\python -m pytest
```
## Functions

- `reynolds(rho, v, D, mu)`: Reynolds number for pipe flow (SI units)

