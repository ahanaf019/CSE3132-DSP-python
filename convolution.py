from signal_operations import *
import matplotlib.pyplot as plt

# h = [1, 2, 0, 2, 1]
# n1 = [-2, -1, 0, 1, 2]

# x = [1, 2, 0, 2, 1]
# n2 = [-2, -1, 0, 1, 2]

def convolution_sum(n1, n2, h, x):

    n1, h = FoldSignal(n1, h)
    nmin = min(n2) - max(n1)
    nmax = max(n2) + len(n1)

    n = []
    res = []
    i = nmin
    while i != nmax + 1:
        nr, xr = ShiftSignal(n1, h, i)
        nm, xm = MultiplySignals(nr, n2, xr, x)
        res.append(sum(xm))
        n.append(i)
        i+=1
    return n, res



# n, y = convolution_sum(n1, n2, h, x)
# plt.stem(n, y)
# plt.show()


