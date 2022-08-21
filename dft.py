import math
from math import pi
import math
import matplotlib.pyplot as plt
from analog_signal import SinSignal

x = []
t = []
i = 0
while i <= 1:
    t.append(i)
    sig = math.sin(2 * pi * 1 * i) + 0.5 * math.sin(2 * pi * 2 * i + 3*pi/4)
    x.append(sig)    
    i += .00001


plt.plot(t, x)
# plt.show()


fs = 8
T = 1/fs

nmin = math.ceil(min(t)/T)
nmax = math.floor(max(t)/T)
print(nmin, nmax)
n = []
xs = []
for i in range(nmin, nmax + 1):
    n.append(i*T)
    sig = math.sin(2 * pi * 1 * i*T) + 0.5 * math.sin(2 * pi * 2 * i*T + 3*pi/4)
    xs.append(sig)


plt.plot(n, xs, '.r')
plt.show()

