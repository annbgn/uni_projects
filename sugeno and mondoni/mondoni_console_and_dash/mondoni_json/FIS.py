import numpy as np
import BasicFuzzyFunctions as bf
import json as j


class MFunction(object):
    def __init__(self, d):
        self.FType = d["FType"]
        self.Params = d["Params"]

    def Calc(self, x):
        if self.FType == "Trap":
            return bf.Trap(
                x,
                self.Params["a"],
                self.Params["b"],
                self.Params["c"],
                self.Params["d"],
            )
        elif self.FType == "S":
            return bf.S(x, self.Params["a"], self.Params["b"])
        elif self.FType == "Z":
            return bf.Z(x, self.Params["a"], self.Params["b"])
        elif self.FType == "SmTrap":
            return bf.SmTrap(
                x,
                self.Params["a"],
                self.Params["b"],
                self.Params["c"],
                self.Params["d"],
            )
        elif self.FType == "SmS":
            return bf.SmS(x, self.Params["a"], self.Params["b"])
        elif self.FType == "SmZ":
            return bf.SmZ(x, self.Params["a"], self.Params["b"])
        else:
            return 0


class LTerm(object):
    def __init__(self, d):
        self.MFunc = MFunction(d["MFunc"])
        self.Value = d["Value"]


class Variable(object):
    def __init__(self, d):
        self.LeftB = d["LeftB"]
        self.RightB = d["RightB"]
        self.LTerms = {t: LTerm(d["LTerms"][t]) for t in d["LTerms"]}
        self.Value = d["Value"]
        self.NumberOfPoints = d["NumberOfPoints"]
        self.ArgArray = np.array([])
        self.ValArray = np.array([])


class Literal(object):
    def __init__(self, d, Vars):
        self.Var = Vars[d["VarName"]]
        self.LTName = d["LTName"]
        self.Neg = d["Neg"]

    def Calc(self):
        X = self.Var
        import pdb

        pdb.set_trace()
        T = X.LTerms[self.LTName]
        v = T.Value
        if self.Neg:
            v = 1 - v
        return v


class Conjunct(object):
    def __init__(self, c, Vars):
        self.Literals = [Literal(l, Vars) for l in c]

    def Calc(self):
        return min([L.Calc() for L in self.Literals])


class Disjunct(object):
    def __init__(self, d, Vars):
        self.Conjuncts = [Conjunct(c, Vars) for c in d]

    def Calc(self):
        return max([c.Calc() for c in self.Conjuncts])


class FIS(object):
    def __init__(self, d):
        self.Inputs = {n: Variable(d["Inputs"][n]) for n in d["Inputs"]}
        self.Outputs = {n: Variable(d["Outputs"][n]) for n in d["Outputs"]}
        self.Productions = {
            y: {
                l: Disjunct(d["Productions"][y][l], self.Inputs)
                for l in self.Outputs[y].LTerms
            }
            for y in self.Outputs
        }
        self.DefMethod = d["DefMethod"]

    def Fuzzyfication(self):
        for x in self.Inputs:
            X = self.Inputs[x]
            for t in X.LTerms:
                T = X.LTerms[t]
                MF = T.MFunc
                T.Value = MF.Calc(X.Value)

    def FuzzyInference(self):
        for y in self.Outputs:
            Y = self.Outputs[y]
            for t in Y.LTerms:
                T = Y.LTerms[t]
                P = self.Productions[y][t]
                T.Value = P.Calc()

    def Composition(self):
        for y in self.Outputs:
            Y = self.Outputs[y]
            N = Y.NumberOfPoints
            a = Y.LeftB
            b = Y.RightB
            Y.ArgArray = np.linspace(a, b, N)
            Y.ValArray = [
                max(
                    [
                        min(Y.LTerms[t].Value, Y.LTerms[t].MFunc.Calc(x))
                        for t in Y.LTerms
                    ]
                )
                for x in Y.ArgArray
            ]

    def Defuzzyfication(self):
        for y in self.Outputs:
            Y = self.Outputs[y]
            if self.DefMethod == "FirstMax":
                DM = bf.FirstMax
            elif self.DefMethod == "LastMax":
                DM = bf.LastMax
            elif self.DefMethod == "AvgMax":
                DM = bf.AvgMax
            else:
                DM = bf.Centroid
            Y.Value = DM(Y.ArgArray, Y.ValArray)

    def Run(self):
        self.Fuzzyfication()
        self.FuzzyInference()
        self.Composition()
        self.Defuzzyfication()


def FISfromJSON(FileName):
    with open(FileName, "r") as f:
        d = j.load(f)
    return FIS(d)
