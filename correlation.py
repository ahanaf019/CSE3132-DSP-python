from signal_operations import *
import matplotlib.pyplot as plt

x = [0, 0, 2, -1, 3, 7, 1, 2, -3, 0, 0]
n1 = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

y = [0, 0, 1, -1, 2, -2, 4, 1, -2, 5, 0, 0]
n2 = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

def CrossCorrelation(n1, n2, x, y):
    n = []
    res = []

    nmin = min(n2) - max(n1)
    nmax = max(n2) + len(n1)

    i = nmin
    while i != nmax + 1:

        ns, xs = ShiftSignal(n2, y, i)

        nr, xr = MultiplySignals(ns, n1, xs, x)
        res.append(sum(xr))
        n.append(i)
        i += 1
    return n, res



def AutoCorrelation(n1, x):
    n = []
    res = []

    nmin = min(n1) - max(n1)
    nmax = max(n1) + len(n1)

    i = nmin
    while i != nmax + 1:

        ns, xs = ShiftSignal(n1, x, i)

        nr, xr = MultiplySignals(ns, n1, xs, x)
        res.append(sum(xr))
        n.append(i)
        i += 1
    return n, res



n, x = CrossCorrelation(n1, n2, x, y)
plt.stem(n, x)
plt.show()