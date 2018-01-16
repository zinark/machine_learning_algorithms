import collections
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cross_validation, neighbors
import random

import Library.CoreML


def k_nearest_neighbors(data, predict, k=3):
    # radius'ten hepsini karsilastirmayabiliriz
    if len(data) >= k:
        warnings.warn('not enough data for classifying %d items' % k)

    distances = []
    for group in data:
        for flist in data[group]:
            diff = np.array(flist) - np.array(predict)
            # euclidean_distance = np.sqrt(np.sum(diff ** 2))
            euclidean_distance = np.linalg.norm(diff)
            distances.append([euclidean_distance, group])

    distances = sorted(distances, reverse=False)[0:k]
    group_labels = map(lambda x: x[1], distances)
    most_common_tuple = collections.Counter(group_labels).most_common(1)
    most_common = most_common_tuple[0][0]
    confidence = most_common_tuple[0][1] / float(k)
    return most_common, confidence


acc_report = {
    "scikit": [],
    "custom": []
}
for i in range(5):
    df = pd.read_csv('data/breast-cancer.data')
    df.replace('?', -99999, inplace=True)
    df = df.astype(float)

    features = np.array(df.drop(['Class', 'Id'], 1))
    labels = np.array(df['Class'])

    XTrain, XTest, YTrain, YTest = cross_validation.train_test_split(features, labels, test_size=0.3)
    clf = neighbors.KNeighborsClassifier(n_neighbors=5, n_jobs=1, radius=1)
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
        #result, confidence = k_nearest_neighbors(trained_data, value, k=5)
        result, confidence = Library.CoreML.CoreML.knn(trained_data, value, k=5, radius=1)
        if result == key:
            correct += 1
        else:
            # algorithm %un-confidency.
            # Secmedim ama %60 digerine kaydigi icin secmedim
            # print result, confidence
            pass
        total += 1

    custom_score = correct / total

    print "scikit - knn score = ", scikit_score
    acc_report["scikit"].append(scikit_score)
    print "custom - knn score = ", custom_score
    acc_report["custom"].append(custom_score)

print "scikit - avg = ", np.mean(acc_report["scikit"])
print "custom - avg = ", np.mean(acc_report["custom"])
