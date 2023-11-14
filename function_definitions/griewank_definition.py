import numpy as np


def GriewankFunction(x, y):
    term1 = 1 + (x**2 / 4000) + (y**2 / 4000)
    term2 = np.cos(x) * np.cos(y / np.sqrt(2))
    return term1 - term2