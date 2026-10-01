def reynolds(rho, v, D, mu):
    """Reynolds number for pipe flow. SI units: kg/m3, m/s, m, Pa s."""
    if min(rho, v, D, mu) <= 0:
        raise ValueError("all inputs must be positive")
    return rho * v * D / mu


def flow_regime(re):
    """Pipe-flow regime: laminar below 2300, turbulent above 4000."""
    if re < 2300:
        return "laminar"
    if re <= 4000:
        return "transitional"
    return "turbulent"