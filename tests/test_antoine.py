import pytest

from chemeng.thermo import antoine_pressure

# Antoine constants for water, P in mmHg, T in degC, valid up to 100 degC.
# Source: Wikipedia, "Antoine equation", example parameters table.
WATER = (8.07131, 1730.63, 233.426)


def test_water_normal_boiling_point():
    # By definition water boils at ~760 mmHg (1 atm) at 100 degC.
    assert antoine_pressure(100, *WATER) == pytest.approx(760, rel=1e-3)


def test_water_at_25C():
    # Steam tables: 3.17 kPa = 23.8 mmHg at 25 degC.
    assert antoine_pressure(25, *WATER) == pytest.approx(23.8, rel=1e-2)