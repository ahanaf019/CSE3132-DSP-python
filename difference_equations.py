from signal_operations import *
from digital_signal import *
import matplotlib.pyplot as plt

def SixPointAveraging(n1, x1):
    n = n1
    x = x1

    for i in range(1, 6):
        ns, xs = ShiftSignal(n1, x1, i)
        n, x = AddSignals(ns, n, xs, x)
    n, x = ScalerMultiply(n, x, 1/6)
    return n, x


def SixPointDifferencing(n1, x1):
    n = n1
    x = x1

    for i in range(1, 6):
        if i%2 == 0:
            mul_val = 1
        else: 
            mul_val = -1

        ns, xs = ShiftSignal(n1, x1, i)
        nr, xr = ScalerMultiply(ns, xs, mul_val)
        nr, xr = AddSignals(ns, nr, xs, xr)
        n, x = AddSignals(n, nr, x, xr)
    n, x = ScalerMultiply(n, x, 1/6)
    return n, x


def RecursiveLowPass(n1, x1):
    pass




# n, x = ExpSignal(0.8, -10, 10)
# plt.subplot(4,1,1)
# plt.stem(n, x)

n, x = UnitStepSignal(-2, 10, 2)
plt.subplot(3,1,1)
plt.stem(n, x)
plt.title("Main Signal")

n, x = SixPointAveraging(n, x)
plt.subplot(3,1,2)
plt.stem(n, x)
plt.title("6 Point Averaging Filter")

n, x = SixPointDifferencing(n, x)
plt.subplot(3,1,3)
plt.stem(n, x)
plt.title("6 Point Differencing Filter")


plt.show()
