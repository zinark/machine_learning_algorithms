import collections
import math
import numpy as np


class CoreML:

    def __init__(self):
        pass

    @staticmethod
    def euclidean_distance(v1, v2=None):
        dimension = len(v1)
        if not v2:
            v2 = [0] * dimension
        sumtotal = 0
        for i in range(dimension):
            sumtotal += (v1[i] - v2[i]) ** 2
        return math.sqrt(sumtotal)

    @staticmethod
    def dot_products(v1, v2):
        dimension = len(v1)
        sumtotal = 0
        for i in range(dimension):
            sumtotal += v1[i] * v2[i]
        return sumtotal

    @staticmethod
    def knn(data_by_classes, input_data, k=5, radius=None):
        distances = []

        for group in data_by_classes:
            all_features = data_by_classes[group]
            diffs = np.array(all_features) - np.array(input_data)
            for diff in diffs:
                euclidean_distance = np.linalg.norm(diff)  # euclidean_distance = np.sqrt(np.sum(diff ** 2))
                if radius and radius <= euclidean_distance:
                    distances.append([euclidean_distance, group])

                if not radius:
                    distances.append([euclidean_distance, group])

        distances = sorted(distances, reverse=False)[0:k]
        labels = map(lambda x: x[1], distances)

        most_common_tuple = collections.Counter(labels).most_common(1)
        if not most_common_tuple: return 0, 0
        most_common = most_common_tuple[0][0]
        confidence = most_common_tuple[0][1] / float(k)
        return most_common, confidence
