from dft import *
import math
from math import pi
import matplotlib.pyplot as plt


x = []
t = []

# Point dft
point = 64

# Signal frequencies
f1 = 10
f2 = 20

# Signal amplitudes
a1 = 1
a2 = 0.5

# Sampling frequency
fs = 80

# Signal generation
i = 0
while i <= 2:
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


c, X, N = dft(n, xs, fs, point=point, norm=True)
# print(N)
plt.subplot(2,1,2)
plt.stem(c, N)

print(len(c))


n, x = inv_dft(c, X, point=point)

for i in range(0, len(n)):
    n[i] = n[i]*T


plt.subplot(2,1,1)
plt.plot(n, x, '.y')
print(x)




plt.show()