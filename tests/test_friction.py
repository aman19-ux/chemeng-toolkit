import math

import pytest

from chemeng.flow import darcy_friction


def test_laminar_uses_64_over_re():
    assert darcy_friction(1000, 0.001) == pytest.approx(0.064)


def test_satisfies_colebrook_equation():
    re, rr = 1e5, 1e-4
    f = darcy_friction(re, rr)
    rhs = -2 * math.log10(rr / 3.7 + 2.51 / (re * math.sqrt(f)))
    assert 1 / math.sqrt(f) == pytest.approx(rhs, rel=1e-9)


def test_fully_rough_limit():
    # At very high Re, Colebrook tends to 1/sqrt(f) = -2 log10(rr / 3.7).
    rr = 1e-3
    expected = (-2 * math.log10(rr / 3.7)) ** -2
    assert darcy_friction(1e12, rr) == pytest.approx(expected, rel=1e-4)


def test_agrees_with_haaland():
    # Haaland's explicit approximation is within about 2% of Colebrook.
    re, rr = 1e5, 1e-4
    haaland = (-1.8 * math.log10((rr / 3.7) ** 1.11 + 6.9 / re)) ** -2
    assert darcy_friction(re, rr) == pytest.approx(haaland, rel=2e-2)


def test_rejects_bad_input():
    with pytest.raises(ValueError):
        darcy_friction(-1, 0.001)