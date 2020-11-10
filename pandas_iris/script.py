import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_bool_dtype
from utils import grouper
from tabulate import tabulate


file = pd.read_csv("./data/iris.data")
# file = pd.read_csv("./data/iris.names")

cols = [
    "sepal length in cm",
    "sepal width in cm",
    "petal length in cm",
    "petal width in cm",
    "class",
]
file.columns = cols
file_no_numeric = file.__deepcopy__()

# all numeric to nominal
for i in file_no_numeric.columns:
    if is_numeric_dtype(file_no_numeric[i]):
        lower = np.percentile(file_no_numeric[i], 33)
        higher = np.percentile(file_no_numeric[i], 66)
        file_no_numeric[i] = [grouper(x, lower, higher) for x in file_no_numeric[i]]


# all nominal to boolean
file_no_nominal = file_no_numeric.__deepcopy__()
cols = file.columns.copy()
cols_to_delete = []
for i in cols:
    cols_to_add = []
    if not is_bool_dtype(file_no_nominal[i]):
        cols_to_delete.append(i)
        cols_to_add = file_no_nominal[i].unique()
        for j in cols_to_add:
            values = list(map(lambda x: True if x == j else False, file_no_nominal[i]))
            file_no_nominal.insert(file_no_nominal.shape[1]-1, i+' '+j, values)

file_no_nominal = file_no_nominal.drop(columns=cols_to_delete)


print("INITIAL DATASET")
print("_" * 20)
print(tabulate(file, file.columns, tablefmt="pretty", showindex=False))
print()

print("NO NUMERIC DATASET")
print("_" * 20)
print(tabulate(file_no_numeric, file_no_numeric.columns, tablefmt="pretty", showindex=False))

print("NO NOMINAL DATASET")
print("_" * 20)
print(tabulate(file_no_nominal, file_no_nominal.columns, tablefmt="pretty", showindex=False))
