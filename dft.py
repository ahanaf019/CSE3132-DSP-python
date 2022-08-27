import math
from math import pi
import math
import matplotlib.pyplot as plt
from analog_signal import SinSignal



def dft(n1, x1, fs, point, norm=False):
    X = []
    N = []
    c = []
    res = fs/point
    x1 = x1[0:point]

    for i in range(0, point):
        X.append(0)
        N.append(0)
        c.append(i*res)

        for j in range(0, point):
            tmp = x1[j] * math.e**(-1j * 2 * math.pi * i * j/point)
            X[i] += tmp
            # print(i, tmp)
        if norm:
            N[i] = abs(X[i])
    return c, X, N


def inv_dft(n1, x1, point):
    x = []
    n = []

    for i in range(0, point):
        x.append(0)
        n.append(i)
        for j in range(0, point):
            x[i] += x1[j] * math.e**(1j * 2 * math.pi * i * j/point)
  
        x[i] /= point
        x[i] = abs(x[i])
    return n, x
