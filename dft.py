import math
from math import pi
import math
import matplotlib.pyplot as plt
from analog_signal import SinSignal



def dft(n1, x1, fs, point):
    X = []
    c = []
    res = fs/point
    x1 = x1[0:point]

    for i in range(0, point):
        X.append(0)
        c.append(i*res)

        for j in range(0, point):
            tmp = x1[j] * math.e**(-1j * 2 * math.pi * i * j/point)
            X[i] += tmp
            # print(i, tmp)

        X[i] = abs(X[i])
    return c, X