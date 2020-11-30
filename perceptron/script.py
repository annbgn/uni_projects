import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from tabulate import tabulate
import random

# reasd file
file = pd.read_csv("./data/glass_c.data")

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
train = file_no_nominal.sample(frac=0.8, random_state=200)
test = file_no_nominal.drop(train.index)

# select desired input and output columns
train_input = train.iloc[:, : -len(classes)]
train_output = train.iloc[:, -len(classes) :]
test_input = test.iloc[:, : -len(classes)]
test_output = test.iloc[:, -len(classes) :]


# perceptron
learning_rate = 0.01
epochs_amount = 1000
which_class = "containers"
# single layer
attributes_amount = train_input.shape[1] - 2
initial_weights = np.ones(shape=train_input.shape[1] - 2)
bias = 7


def proceed(input_attributes):
    net = 0
    for i in range(attributes_amount):
        net += int(input_attributes[i]) * initial_weights[i]
    return net >= bias


# todo one func from increase and decrease
def decrease(input_attributes):
    for i in range(attributes_amount):
        if input_attributes[i] == 1:
            initial_weights[i] -= 1


def increase(input_attributes):
    for i in range(attributes_amount):
        if input_attributes[i] == 1:
            initial_weights[i] += 1


for i in range(epochs_amount):
    # выберем случайный элемент обучаюзей выборки
    option = random.randint(0, file_no_indices.shape[0])
    # Если получилось наше значение which_class
    if file_no_indices.iloc[option]["class_" + which_class] != 1:
        # Если сеть выдала True, то наказываем ее
        if proceed(file_no_indices.iloc[option][: -len(classes)]):
            decrease(file_no_indices["class_" + which_class].iloc[:, : -len(classes)])
    else:
        # Если сеть выдала False, то добавляем веса
        if not proceed([]):
            increase([])

print(
    tabulate(
        file_no_nominal,
        file_no_nominal.columns,
        showindex=False,
        # tablefmt="pretty",
    )
)
