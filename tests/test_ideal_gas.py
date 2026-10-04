import pytest

from chemeng.thermo import ideal_gas


def test_molar_volume_at_stp():
    # 1 mol at 273.15 K and 101325 Pa occupies about 22.414 L.
    assert ideal_gas(P=101325, n=1, T=273.15) == pytest.approx(0.022414, rel=1e-4)


def test_solves_for_pressure():
    assert ideal_gas(V=0.022414, n=1, T=273.15) == pytest.approx(101325, rel=1e-4)


def test_solves_for_moles_and_temperature():
    assert ideal_gas(P=101325, V=0.022414, T=273.15) == pytest.approx(1, rel=1e-4)
    assert ideal_gas(P=101325, V=0.022414, n=1) == pytest.approx(273.15, rel=1e-4)


def test_needs_exactly_one_unknown():
    with pytest.raises(ValueError):
        ideal_gas(P=101325, n=1)