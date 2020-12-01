import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from tabulate import tabulate
import random

# reasd file
file = pd.read_csv("./data/glass.data")

# from glass.names
classes = [
    "building_windows_float_processed",
    "building_windows_non_float_processed",
    "vehicle_windows_float_processed",
    "vehicle_windows_non_float_processed(none in this database)",
    "containers",
    "tableware",
    "headlamps",
]

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
    elif idx == 10:
        file_no_numeric[i] = pd.cut(
            file_no_numeric[i],
            labels=classes,
            bins=len(classes),
        )

# nominal to binary
file_no_nominal = pd.get_dummies(file_no_numeric, dtype=int)

# 0 and 1 -> -1 and 1
for idx, i in enumerate(file_no_nominal):
    if idx not in [0, 1]:
        file_no_nominal[i] = list(map(lambda x: 1 if x else -1, file_no_nominal[i]))

# remove id and index
file_no_indices = file_no_nominal.drop(["id", "refractive index"], 1)

# split into train and test
train = file_no_indices.sample(frac=0.8, random_state=200)
test = file_no_indices.drop(train.index)

# select desired input and output columns
train_input = train.iloc[:, : -len(classes)]
train_output = train.iloc[:, -len(classes) :]
test_input = test.iloc[:, : -len(classes)]
test_output = test.iloc[:, -len(classes) :]


# perceptron
learning_rate = 0.01
epochs_amount = 100
which_class = "containers"
# single layer
attributes_amount = train_input.shape[1] - 2
initial_weights = np.ones(shape=train_input.shape[1])
bias = 7


def proceed(input_attributes):
    net = 0
    for idx, attribute in enumerate(input_attributes.iteritems()):
        if isinstance(attribute[1], int):
            net += int(attribute[1]) * initial_weights[idx]
        else:
            net += int(attribute[1].item()) * initial_weights[idx]
    return net >= bias


# todo one func from increase and decrease
def decrease(input_attributes):
    for idx, attribute in enumerate(input_attributes.iteritems()):
        if int(attribute[1].item()) == 1:
            initial_weights[idx] -= 1


def increase(input_attributes):
    for idx, attribute in enumerate(input_attributes.iteritems()):
        if int(attribute[1].item()) == 1:
            initial_weights[idx] += 1


# train
for epoch in range(epochs_amount):
    # select a random element from train set
    chosen_elem = train.iloc[[random.randint(0, train.shape[0] - 1)]]
    chosen_attributes = chosen_elem.iloc[:, : -len(classes)]

    # if chosen elem is belongs to chosen class
    if chosen_elem["class_" + which_class].item() != 1:
        # if it was not classified as chosen class, decrease weights
        if not proceed(chosen_attributes):
            decrease(chosen_attributes)
    else:
        # if chosen elem does not belong to chosen class, but was classified to it, increase weights
        if proceed(chosen_attributes):
            increase(chosen_attributes)

# test
success = 0
failure = 0
for row in test.iterrows():
    chosen_attributes = row[1].iloc[: -len(classes)]
    is_classified = proceed(chosen_attributes)
    if (
        is_classified
        and row[1]["class_" + which_class].item() == 1
        or not is_classified
        and row[1]["class_" + which_class].item() == -1
    ):
        success += 1
    else:
        failure += 1


print("success: ", success)
print("failure: ", failure)
