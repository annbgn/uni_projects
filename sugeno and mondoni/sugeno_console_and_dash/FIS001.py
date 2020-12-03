"""
Budget -> Fees
Star -> Oscar
"""
from MFFunctions001 import *

global Budget, Star, Oscar, Fees
Budget = Star = Oscar = Fees = 0
BudgetGreat = (
    BudgetHigh
) = (
    BudgetAverage
) = (
    BudgetLow
) = (
    StarHigh
) = (
    StarAverage
) = StarLow = OscarExcellent = OscarGood = OscarSatisfactory = OscarBad = 0
OscarArray = {x: 0 for x in range(20, 51)}


def Fuzzification():
    global Budget, Star
    global BudgetGreat, BudgetHigh, BudgetAverage, BudgetLow, StarHigh, StarAverage, StarLow, FeesGreat, FeesHigh, FeesAverage, FeesLow

    FeesGreat = mfFeesGreat(Budget)
    FeesHigh = mfFeesHigh(Budget)
    FeesAverage = mfFeesAverage(Budget)
    FeesLow = mfFeesLow(Budget)
    StarHigh = mfStarHigh(Star)
    StarAverage = mfStarAverage(Star)
    StarLow = mfStarLow(Star)


def FuzzyInference():
    global BudgetGreat, BudgetHigh, BudgetAverage, BudgetLow, StarHigh, StarAverage, StarLow, OscarExcellent, OscarGood, OscarSatisfactory, OscarBad, FeesGreat, FeesHigh, FeesAverage, FeesLow

    OscarExcellent = min(BudgetGreat, StarLow)
    OscarGood = max(min(BudgetGreat, StarAverage), min(BudgetHigh, StarLow))
    OscarSatisfactory = max(
        min(BudgetGreat, StarHigh),
        min(BudgetHigh, StarAverage),
        min(BudgetAverage, StarLow),
    )
    OscarBad = max(BudgetLow, min(StarHigh, 1 - BudgetGreat))


def Composition():
    global OscarExcellent, OscarGood, OscarSatisfactory, OscarBad
    global OscarArray

    for i in range(20, 51):
        OscarArray[i] = max(
            min(mfOscarExcellent(i / 10), OscarExcellent),
            min(mfOscarGood(i / 10), OscarGood),
            min(mfOscarSatisfactory(i / 10), OscarSatisfactory),
            min(mfOscarBad(i / 10), OscarBad),
        )


def Defuzzyfication():
    global Oscar
    global OscarArray

    X = list(OscarArray.keys())
    Y = list(OscarArray.values())

    Oscar = LastMax(X, Y) / 10


def Run():
    Fuzzification()
    FuzzyInference()
    Composition()
    Defuzzyfication()


def Init():
    global Budget, Star

    Budget = float(input("Budget = "))
    Star = float(input("Star = "))


def Terminate():
    global Oscar
    Fees = (
        FeesGreat * 1000 * Budget
        + FeesHigh * 100 * Budget
        + FeesLow * 10 * Budget
        + FeesLow * Budget
    ) / (FeesGreat + FeesHigh + FeesAverage + FeesLow)

    print("Oscar =", Star)
    print("Fees =", Fees)


def Main():
    if __name__ == "__main__":
        Init()
    Run()
    Terminate()


if __name__ == "__main__":
    Main()
