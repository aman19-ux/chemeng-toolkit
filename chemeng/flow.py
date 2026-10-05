import math

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

def darcy_friction(re, rel_roughness, tol=1e-10, max_iter=100):
    """Darcy friction factor for pipe flow.

    Laminar (Re < 2300): f = 64 / Re.
    Otherwise solves the Colebrook equation by fixed-point iteration on x = 1/sqrt(f):
        x = -2 log10(rel_roughness / 3.7 + 2.51 x / Re)
    rel_roughness is epsilon / D (dimensionless).powe
    """
    if re <= 0 or rel_roughness < 0:
        raise ValueError("Re must be positive and roughness non-negative")
    if re < 2300:
        return 64 / re
    x = 7.0  # initial guess, f ~ 0.02
    for _ in range(max_iter):
        x_new = -2 * math.log10(rel_roughness / 3.7 + 2.51 * x / re)
        if abs(x_new - x) < tol:
            return 1 / x_new**2
        x = x_new
    raise RuntimeError("Colebrook iteration did not converge")

G = 9.80665  # m/s2, standard gravity (exact by definition)


def pump_power(rho, Q, H, efficiency):
    """Shaft power in W to deliver flow Q (m3/s) against head H (m)."""
    if not 0 < efficiency <= 1:
        raise ValueError("efficiency must be in (0, 1]")
    return rho * G * Q * H / efficiency

