import math
from digital_signal import *


def AddSignals(n1, n2, x1, x2):
    nmin = min(min(n1), min(n2))
    nmax = max(max(n1), max(n2))
    n = []
    y1 = []
    y2 = []
    y1c = False
    y2c = False

    i = nmin
    while(i <= nmax):
        n.append(i)

        if i >= min(n1) and i <= max(n1):
            if(not y1c):
                    for elem in x1:
                        y1.append(elem)
                    y1c = True
        else:
            y1.append(0)
        
        if i >= min(n2) and i <= max(n2):
            if(not y2c):
                    for elem in x2:
                        y2.append(elem)
                    y2c = True
        else:
            y2.append(0)
        i += 1

    y = []
    for i in range(0, len(n)):
        y.append(y1[i] + y2[i])
    
    return n, y


def MultiplySignals(n1, n2, x1, x2):
    nmin = min(min(n1), min(n2))
    nmax = max(max(n1), max(n2))
    
    n = []
    y1 = []
    y2 = []
    y1c = False
    y2c = False

    i = nmin
    while(i <= nmax):
        n.append(i)

        if i >= min(n1) and i <= max(n1):
            if(not y1c):
                    for elem in x1:
                        y1.append(elem)
                    y1c = True
        else:

            y1.append(0)
        
        if i >= min(n2) and i <= max(n2):
            if(not y2c):
                    for elem in x2:
                        y2.append(elem)
                    y2c = True
        else:
            y2.append(0)
        i += 1

    y = []
    for i in range(0, len(n)):
        y.append(y1[i] * y2[i])
    
    return n, y

def ScalerMultiply(n1, x1, multiply_value):
    n = n1
    x = []
    for xs in x1:
        x.append(xs * multiply_value)
    return n, x

def FoldSignal(n1, x1):
    x = x1
    n = []
    for ns in n1:
        n.append(-1 * ns)
    x = x[::-1]
    n = n[::-1]
    return n, x

def ShiftSignal(n1, x1, shift_val):
    x = x1
    n = []

    for ns in n1:
        n.append(ns + shift_val)
    return n, x
    
    
def GetValueAtPoint(n, x, point):
    if point < min(n) or point > max(n):
        print('INDEX OUT OF BOUND')
        return
    
    if len(n) != len(x):
        print('INVALID SIGNAL')
        return

    for i in range(0, len(n)):
        if n[i] == point:
            return x[i]
    return -99999999

def SliceSignal(n1, x1, start, end):
    n = []
    x = []

    for i in range (0, len(n1)):
        if i >= start and i <= end:
            n.append(i)
            x.append(x1[i])
    
    return n, x
