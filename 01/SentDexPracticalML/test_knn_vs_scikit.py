import collections
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cross_validation, neighbors
import random

df = pd.read_csv('data/breast-cancer.data')
df.replace('?', -99999, inplace=True)
df = df.astype(float)


def k_nearest_neighbors(data, predict, k=3):
    # radius'ten hepsini karsilastirmayabiliriz
    if len(data) >= k:
        warnings.warn('not enough data for classifying ' + k + ' items')

    distances = []
    for group in data:
        for flist in data[group]:
            diff = np.array(flist) - np.array(predict)
            # euclidean_distance = np.sqrt(np.sum(diff ** 2))
            euclidean_distance = np.linalg.norm(diff)
            distances.append([euclidean_distance, group])

    distances = sorted(distances, reverse=False)[0:k]
    group_labels = map(lambda x: x[1], distances)
    most_common = collections.Counter(group_labels).most_common(1)
    return most_common[0][0]


features = np.array(df.drop(['Class', 'Id'], 1))
labels = np.array(df['Class'])

XTrain, XTest, YTrain, YTest = cross_validation.train_test_split(features, labels, test_size=0.25)
clf = neighbors.KNeighborsClassifier()
clf.fit(XTrain, YTrain)
scikit_score = clf.score(XTest, YTest)


trained_data = {}

for i in range(len(XTrain)):
    key = YTrain[i]
    value = XTrain[i]

    if not trained_data.has_key(key):
        trained_data[key] = []
    trained_data[key].append(value)

correct = 0.
total = 0.

for i in range(len(XTest)):
    key = YTrain[i]
    value = XTrain[i]
    result = k_nearest_neighbors(trained_data, value, k=5)
    if result == key:
        correct += 1
    total += 1

custom_score = correct / total

print "scikit - knn score = ", scikit_score
print "custom - knn score = ", custom_score
