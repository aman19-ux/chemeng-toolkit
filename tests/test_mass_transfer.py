import pytest

from chemeng.mass_transfer import operating_line


def test_line_passes_through_both_column_ends():
    # Mass balance Gs (Y1 - Y2) = Ls (X1 - X2) fixes the bottom composition.
    Ls, Gs = 100, 50
    X2, Y2 = 0.0, 0.002  # top: lean liquid in, clean gas out
    X1 = 0.04  # bottom: rich liquid out
    Y1 = Y2 + Ls / Gs * (X1 - X2)  # bottom: rich gas in = 0.082
    slope, intercept = operating_line(Ls, Gs, X1, Y1)
    assert slope == pytest.approx(2.0)
    assert slope * X2 + intercept == pytest.approx(Y2)


def test_rejects_non_positive_flow():
    with pytest.raises(ValueError):
        operating_line(0, 50, 0.04, 0.082)