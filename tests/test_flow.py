import pytest

from chemeng.flow import flow_regime, reynolds


def test_reynolds_water_in_pipe():
    assert reynolds(1000, 1.0, 0.05, 1e-3) == pytest.approx(40_000)


def test_reynolds_rejects_non_positive():
    with pytest.raises(ValueError):
        reynolds(1000, 1.0, 0.05, 0)


@pytest.mark.parametrize(
    "re, expected",
    [(1000, "laminar"), (2300, "transitional"), (4000, "transitional"), (4001, "turbulent")],
)
def test_flow_regime(re, expected):
    assert flow_regime(re) == expected