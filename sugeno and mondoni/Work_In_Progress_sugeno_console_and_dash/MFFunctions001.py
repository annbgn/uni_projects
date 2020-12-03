from BasicFuzzyFunctions import *


def mfFeesLow(x):
    return GZ(x, 40, 60)


def mfFeesAverage(x):
    return GTrap(x, 20, 40, 60, 75)


def mfFeesHigh(x):
    return GTrap(x, 40, 60, 90, 100)


def mfFeesGreat(x):
    return GS(x, 80, 90)


def mfStarLow(x):
    return GZ(x, 30, 40)


def mfStarAverage(x):
    return GTrap(x, 20, 30, 70, 80)


def mfStarHigh(x):
    return GS(x, 60, 70)


def mfOscarBad(x):
    return GZ(x, 2, 3)


def mfOscarSatisfactory(x):
    return GZ(x, 3.5, 4)


def mfOscarGood(x):
    return GTrap(x, 3, 3.5, 4.5, 4.9)


def mfOscarExcellent(x):
    return GS(x, 4, 4.5)
