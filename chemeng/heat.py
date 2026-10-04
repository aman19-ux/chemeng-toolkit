import math


def lmtd(dT1, dT2):
    """Log-mean temperature difference between the two ends of an exchanger."""
    if dT1 <= 0 or dT2 <= 0:
        raise ValueError("temperature differences must be positive")
    if math.isclose(dT1, dT2):
        return dT1
    return (dT1 - dT2) / math.log(dT1 / dT2)