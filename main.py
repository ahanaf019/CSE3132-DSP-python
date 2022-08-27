from dft import dft
import math
from math import pi
import matplotlib.pyplot as plt


x = []
t = []

# Signal frequencies
f1 = 1000
f2 = 2000

# Signal amplitudes
a1 = 1
a2 = 0.5

# Sampling frequency
fs = 4000

# Signal generation
i = 0
while i <= 1:
    t.append(i)
    sig = a1 * math.sin(2 * pi * f1 * i) + a2 * math.sin(2 * pi * f2 * i + 3*pi/4)
    x.append(sig)    
    i += .00001

plt.subplot(2,1,1)
plt.plot(t, x)


# Sampling
T = 1/fs
nmin = math.ceil(min(t)/T)
nmax = math.floor(max(t)/T)
# print(nmin, nmax)
n = []
xs = []
for i in range(nmin, nmax + 1):
    n.append(i*T)
    sig = a1 * math.sin(2 * pi * f1 * i*T) + a2 * math.sin(2 * pi * f2 * i*T + 3*pi/4)
    xs.append(sig)

plt.plot(n, xs, '.r')


c, X = dft(n, xs, fs, point=16)

plt.subplot(2,1,2)
plt.stem(c, X)
plt.show()