import math

import pytest

from chemeng.heat import lmtd


def test_lmtd_hand_calculation():
    # (60 - 20) / ln(60 / 20) = 40 / ln 3 = 36.41
    assert lmtd(60, 20) == pytest.approx(40 / math.log(3))


def test_lmtd_is_symmetric():
    assert lmtd(20, 60) == pytest.approx(lmtd(60, 20))


def test_lmtd_equal_differences():
    # Limit as dT1 -> dT2: LMTD equals the common temperature difference.
    assert lmtd(30, 30) == pytest.approx(30)


def test_lmtd_rejects_non_positive():
    with pytest.raises(ValueError):
        lmtd(30, 0)