import numpy as np
def AckleyFunction(x, y):
    a = 20
    b = 0.2
    c = 2 * np.pi

    term1 = -a * np.exp(-b * np.sqrt(0.5 * (x ** 2 + y ** 2)))
    term2 = -np.exp(0.5 * (np.cos(c * x) + np.cos(c * y)))

    result = term1 + term2 + a + np.exp(1)
    return result