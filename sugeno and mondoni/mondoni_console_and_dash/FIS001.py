from MFFunctions001 import *

Temperature = Humidity = Comfort = 0
TemperatureGreat = (
    TemperatureHigh
) = (
    TemperatureAverage
) = (
    TemperatureLow
) = (
    HumidityHigh
) = (
    HumidityAverage
) = HumidityLow = ComfortExcellent = ComfortGood = ComfortSatisfactory = ComfortBad = 0
ComfortArray = {x: 0 for x in range(20, 51)}


def Fuzzification():
    global Temperature, Humidity
    global TemperatureGreat, TemperatureHigh, TemperatureAverage, TemperatureLow, HumidityHigh, HumidityAverage, HumidityLow

    TemperatureGreat = mfTemperatureGreat(Temperature)
    TemperatureHigh = mfTemperatureHigh(Temperature)
    TemperatureAverage = mfTemperatureAverage(Temperature)
    TemperatureLow = mfTemperatureLow(Temperature)
    HumidityHigh = mfHumidityHigh(Humidity)
    HumidityAverage = mfHumidityAverage(Humidity)
    HumidityLow = mfHumidityLow(Humidity)


def FuzzyInference():
    global TemperatureGreat, TemperatureHigh, TemperatureAverage, TemperatureLow, HumidityHigh, HumidityAverage, HumidityLow, ComfortExcellent, ComfortGood, ComfortSatisfactory, ComfortBad

    ComfortExcellent = min(TemperatureGreat, HumidityLow)
    ComfortGood = max(
        min(TemperatureGreat, HumidityAverage), min(TemperatureHigh, HumidityLow)
    )
    ComfortSatisfactory = max(
        min(TemperatureGreat, HumidityHigh),
        min(TemperatureHigh, HumidityAverage),
        min(TemperatureAverage, HumidityLow),
    )
    ComfortBad = max(TemperatureLow, min(HumidityHigh, 1 - TemperatureGreat))


def Composition():
    global ComfortExcellent, ComfortGood, ComfortSatisfactory, ComfortBad
    global ComfortArray

    for i in range(20, 51):
        ComfortArray[i] = max(
            min(mfComfortExcellent(i / 10), ComfortExcellent),
            min(mfComfortGood(i / 10), ComfortGood),
            min(mfComfortSatisfactory(i / 10), ComfortSatisfactory),
            min(mfComfortBad(i / 10), ComfortBad),
        )


def Defuzzyfication():
    global Comfort
    global ComfortArray

    X = list(ComfortArray.keys())
    Y = list(ComfortArray.values())

    Comfort = LastMax(X, Y) / 10


def Run():
    Fuzzification()
    FuzzyInference()
    Composition()
    Defuzzyfication()


def Init():
    global Temperature, Humidity

    Temperature = float(input("Temperature = "))
    Humidity = float(input("Humidity = "))


def Terminate():
    global Comfort

    print("Comfort =", Comfort)


def Main():
    Init()
    Run()
    Terminate()


if __name__ == "__main__":
    Main()
