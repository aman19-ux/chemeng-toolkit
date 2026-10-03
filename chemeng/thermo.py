def antoine_pressure(T, A, B, C):
    """Vapour pressure from the Antoine equation, log10(P) = A - B / (C + T).

    Units of P and T are set by the constants used, e.g. mmHg and degC.
    """
    return 10 ** (A - B / (C + T))
