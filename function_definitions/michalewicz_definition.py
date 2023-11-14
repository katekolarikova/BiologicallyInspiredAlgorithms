import numpy as np

def MichalewiczFunction(x, y):
    return 1 * ((np.sin(x) * np.sin((1 * x ** 2) / np.pi) ** 20) + (np.sin(y) * np.sin((2 * y ** 2) / np.pi) ** 20))