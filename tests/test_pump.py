import pytest

from chemeng.flow import pump_power


def test_pump_power_hand_calculation():
    # 1000 * 9.80665 * 0.01 * 20 / 0.75 = 2615.1 W
    assert pump_power(1000, 0.01, 20, 0.75) == pytest.approx(2615.11, rel=1e-5)


@pytest.mark.parametrize("eta", [0, -0.5, 1.2])
def test_rejects_impossible_efficiency(eta):
    with pytest.raises(ValueError):
        pump_power(1000, 0.01, 20, eta)