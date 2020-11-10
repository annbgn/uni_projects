import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from utils import grouper

file = pd.read_csv("./data/iris.data")
# file = pd.read_csv("./data/iris.names")
file_no_numeric = file.__deepcopy__()

cols = [
    "sepal length in cm",
    "sepal width in cm",
    "petal length in cm",
    "petal width in cm",
    "class",
]
file.columns = cols

# all numeric to nominal
for i in file_no_numeric.columns:
    if is_numeric_dtype(file_no_numeric[i]):
        lower = np.percentile(file_no_numeric[i], 33)
        higher = np.percentile(file_no_numeric[i], 66)
        file_no_numeric[i] = [grouper(x, lower, higher) for x in file_no_numeric[i]]
file_no_nominal = file.__deepcopy__()

# all nominal to boolean
pass

print("INITIAL DATASET")
print("_" * 20)
print(file.to_string(index=False))

print("NO NUMERIC DATASET")
print("_" * 20)
print(file_no_numeric.to_string(index=False))

print("NO NOMINAL DATASET")
print("_" * 20)
print(file_no_nominal.to_string(index=False))
