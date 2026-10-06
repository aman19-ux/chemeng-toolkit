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
- `flow_regime(re)`: laminar, transitional or turbulent for a given Reynolds number
- `antoine_pressure(T, A, B, C)`: vapour pressure from the Antoine equation
- `lmtd(dT1, dT2)`: log-mean temperature difference for a heat exchanger
- `ideal_gas(P, V, n, T)`: solve PV = nRT for whichever variable is left out
- `pump_power(rho, Q, H, efficiency)`: pump shaft power from flow and head
- `darcy_friction(re, rel_roughness)`: Darcy friction factor (laminar or Colebrook)
- `operating_line(Ls, Gs, X1, Y1)`: absorber operating line in solute-free mole ratios

## Install

```
pip install git+https://github.com/aman19-ux/chemeng-toolkit
```

Then `from chemeng.flow import reynolds` in any script or notebook.