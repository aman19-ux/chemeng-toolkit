def antoine_pressure(T, A, B, C):
    """Vapour pressure from the Antoine equation, log10(P) = A - B / (C + T).

    Units of P and T are set by the constants used, e.g. mmHg and degC.
    """
    return 10 ** (A - B / (C + T))


R = 8.314462618  # J/(mol K), exact under the 2019 SI definition


def ideal_gas(P=None, V=None, n=None, T=None):
    """Solve PV = nRT for the one argument left as None. SI units: Pa, m3, mol, K."""
    if [P, V, n, T].count(None) != 1:
        raise ValueError("leave exactly one of P, V, n, T as None")
    if P is None:
        return n * R * T / V
    if V is None:
        return n * R * T / P
    if n is None:
        return P * V / (R * T)
    return P * V / (n * R)