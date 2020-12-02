from BasicFuzzyFunctions import *


def mfTemperatureLow(x):
    return GZ(x, 40, 60)


def mfTemperatureAverage(x):
    return GTrap(x, 20, 40, 60, 75)


def mfTemperatureHigh(x):
    return GTrap(x, 40, 60, 90, 100)


def mfTemperatureGreat(x):
    return GS(x, 80, 90)


def mfHumidityLow(x):
    return GZ(x, 30, 40)


def mfHumidityAverage(x):
    return GTrap(x, 20, 30, 70, 80)


def mfHumidityHigh(x):
    return GS(x, 60, 70)


def mfComfortBad(x):
    return GZ(x, 2, 3)


def mfComfortSatisfactory(x):
    return GZ(x, 3.5, 4)


def mfComfortGood(x):
    return GTrap(x, 3, 3.5, 4.5, 4.9)


def mfComfortExcellent(x):
    return GS(x, 4, 4.5)
