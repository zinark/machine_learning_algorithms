import warnings
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

import Library.CoreML

print style.available
style.use('bmh')

dataset = {
    'k': [[1, 2], [2, 3], [3, 1]],  # Class-1 Features
    'r': [[6, 5], [7, 7], [8, 6]]  # Class-2 Features
}
new_features = [5, 7]

predict = Library.CoreML.CoreML.knn(dataset, new_features)


def plot_results():
    for i in dataset:
        for ii in dataset[i]:
            plt.scatter(ii[0], ii[1], s=100, color=i)
    plt.scatter(new_features[0], new_features[1], color=predict)
    plt.show()


plot_results()


def compare_results_with_scikit():
    pass


compare_results_with_scikit()
