import math

def UnitSampleSequence(start, end, val):
    n = []
    x = []

    i = start
    while i != end+1:
        n.append(i)
        if(i == val):
            x.append(1)
            print(i)
        else:
            x.append(0)
        i += 1
    return n,x


def UnitStepSignal(start, end, val):
    n = []
    x = []
    i = start
    while i != end+1:
        n.append(i)
        if(i >= val):
            x.append(1)
        else:
            x.append(0)
        i += 1
    return n,x


def UnitRampSignal(start, end):
    n = []
    x = []
    i = start
    while i != end+1:
        n.append(i)
        if(i >= 0):
            x.append(i)
        else:
            x.append(0)
        i += 1
    return n,x


def ExpSignal(a, start, end):
    n = []
    x = []
    i = start
    while i != end+1:
        n.append(i)
        x.append(a**i)
        i += 1
    return n,x


ExpSignal(0.8, -2, 15)