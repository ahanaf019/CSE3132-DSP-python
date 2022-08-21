import math
import matplotlib.pyplot as plt


def SinSignal(amplitude, frequency, displacement=0, ran=[0, 1]):
    x = []
    t = []
    i = ran[0]

    while(i <= ran[1]):
        a = amplitude * math.sin(2 * math.pi * frequency * i + displacement)
        x.append(a)
        t.append(i)
        i+=0.00001

    return x, t

def CosSignal(amplitude, frequency, displacement=0, ran=[0, 1]):
    x = []
    t = []
    i = ran[0]

    while(i <= ran[1]):
        a = amplitude * math.cos(2 * math.pi * frequency * i + displacement)
        x.append(a)
        t.append(i)
        i+=0.00001
    return x, t


