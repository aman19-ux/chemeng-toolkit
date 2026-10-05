def operating_line(Ls, Gs, X1, Y1):
    """Absorber operating line in solute-free mole ratios, Y = slope * X + intercept.

    Ls, Gs: solute-free liquid and gas flow rates (mol/s).
    (X1, Y1): liquid and gas compositions at one end of the column.
    Returns (slope, intercept).
    """
    if Ls <= 0 or Gs <= 0:
        raise ValueError("flow rates must be positive")
    slope = Ls / Gs
    return slope, Y1 - slope * X1
