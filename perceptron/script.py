import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype, is_bool_dtype
from tabulate import tabulate

# reasd file
file = pd.read_csv("./data/glass_c.data")

# add headers
cols = [
    "id",
    "refractive index",
    "Na",
    "Mg",
    "Al",
    "Si",
    "K",
    "Ca",
    "Ba",
    "Fe",
    "class",
]
file.columns = cols

# sort by class
file.sort_values(by="class")


# numeric to categorial
file_no_numeric = file.__deepcopy__()
for idx, i in enumerate(file_no_numeric.columns):
    if is_numeric_dtype(file_no_numeric[i]) and not idx in [0, 1, 10]:
        file_no_numeric[i] = pd.cut(
            file_no_numeric[i], labels=["small", "medium", "large"], bins=3
        )

# nominal to binary
file_no_nominal = pd.get_dummies(file_no_numeric, dtype=int)

# 0 and 1 -> -1 and 1
for idx, i in enumerate(file_no_nominal):
    if idx not in [0,1]:
        file_no_nominal[i] = list(map(lambda x: 1 if x else -1 , file_no_nominal[i]))

# split into train and test
train=file_no_nominal.sample(frac=0.8,random_state=200)
test=file_no_nominal.drop(train.index)
import pdb;
pdb.set_trace()


print(
    tabulate(
        file_no_nominal, file_no_nominal.columns, showindex=False , # tablefmt="pretty",
    )
)
