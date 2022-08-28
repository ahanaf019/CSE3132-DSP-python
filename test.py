from signal_operations import *
from correlation import *
from convolution import *
import matplotlib.pyplot as plt

x1 = [0,1,-2,3,-4]
n1 = [0,1,2,3,4]

x2 = [0.5, 1, 2, 1, 0.5]
n2 = [-2,-1,0,1,2]

x = [1,1,2,1]
n = [0,1,2,3]

n, x = AutoCorrelation(n, x)
# n, x = convolution_sum(n1, n2, x1, x2)
# n, x = RemovePadding(n, x)

print(x)
print(n)

plt.subplot(2,1,1)
plt.stem(n, x)

# n, x = CrossCorrelation(n1, n2, x1, x2)
# n, x = RemovePadding(n, x)
# print(x)
# print(n)

# plt.subplot(2,1,2)
# plt.stem(n, x)

plt.show()