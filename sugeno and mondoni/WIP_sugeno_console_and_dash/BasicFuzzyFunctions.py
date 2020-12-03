import numpy as np


def Trap(x, a, b, c, d):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c <= x <= d:
        return (d - x) / (d - c)
    else:
        return 0


def S(x, a, b):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif x >= b:
        return 1
    else:
        return 0


def A(x, a, b, c):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)
    else:
        return 0


def Z(x, a, b):
    if x <= a:
        return 1
    elif a <= x <= b:
        return (b - x) / (b - a)
    else:
        return 0


def GTrap(x, a, b, c, d):
    if a <= x <= (a + b) / 2:
        return 2 * (((x - a) / (b - a)) ** 2)
    elif (a + b) / 2 <= x <= b:
        return 1 - 2 * (((b - x) / (b - a)) ** 2)
    elif b <= x <= c:
        return 1
    elif c <= x <= (c + d) / 2:
        return 1 - 2 * (((x - c) / (d - c)) ** 2)
    elif (c + d) / 2 <= x <= d:
        return 2 * (((d - x) / (d - c)) ** 2)
    else:
        return 0


def GA(x, a, b, c):
    if a <= x <= (a + b) / 2:
        return 2 * (((x - a) / (b - a)) ** 2)
    elif (a + b) / 2 <= x <= b:
        return 1 - 2 * (((b - x) / (b - a)) ** 2)
    elif b <= x <= (b + c) / 2:
        return 1 - 2 * (((x - b) / (c - b)) ** 2)
    elif (b + c) / 2 <= x <= c:
        return 2 * (((c - x) / (c - b)) ** 2)
    else:
        return 0


def GS(x, a, b):
    if a <= x <= (a + b) / 2:
        return 2 * (((x - a) / (b - a)) ** 2)
    elif (a + b) / 2 <= x <= b:
        return 1 - 2 * (((b - x) / (b - a)) ** 2)
    elif x >= b:
        return 1
    else:
        return 0


def GZ(x, a, b):
    if x <= a:
        return 1
    elif a <= x <= (a + b) / 2:
        return 1 - 2 * (((x - a) / (b - a)) ** 2)
    elif (a + b) / 2 <= x <= b:
        return 2 * (((b - x) / (b - a)) ** 2)
    else:
        return 0


def Centroid(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    return sum(X * Y) / sum(Y)


def FirstMax(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    mY = max(Y)
    m = min(np.where(Y == mY)[0])
    return X[m]


def LastMax(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    mY = max(Y)
    m = max(np.where(Y == mY)[0])
    return X[m]


def AvgMax(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    mY = max(Y)
    M = np.where(Y == mY)[0]
    A = [X[i] for i in M]
    A = np.array(A)
    return np.mean(A)
