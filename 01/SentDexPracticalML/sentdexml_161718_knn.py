import warnings
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

print style.available
style.use('bmh')

dataset = {
    'k': [[1, 2], [2, 3], [3, 1]],  # Class-1 Features
    'r': [[6, 5], [7, 7], [8, 6]]  # Class-2 Features
}
new_features = [5, 7]


def k_nearest_neighbors(data, predict, k=3):
    # radius'ten hepsini karsilastirmayabiliriz

    if len(data) >= k: warnings.warn('not enough data for classifying ' + k + ' items')
    distances = []
    for group in data:
        print group, data[group]
        for features in data[group]:
            diff = np.array(features) - np.array(predict)
            # euclidean_distance = np.sqrt(np.sum(diff ** 2))
            euclidean_distance = np.linalg.norm(diff)
            distances.append([euclidean_distance, group])

    distances = sorted(distances, reverse=False)[0:k]
    labels = map(lambda x: x[1], distances)

    # print distances, labels
    mostCommon = Counter(labels).most_common(1)
    return mostCommon[0][0]


predict = k_nearest_neighbors(dataset, new_features)


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
