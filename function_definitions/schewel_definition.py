import numpy as np


def SchewelFunction(x, y):
    n = 2

    term1 = 418.9829 * n
    term2 = -x * np.sin(np.sqrt(np.abs(x)))
    term3 = -y * np.sin(np.sqrt(np.abs(y)))
    return term1 + term2 + term3