import collections
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


class CoreSVM:
    # hyperplane = x . w + b = 0
    # x . w + b =  1     for pos Support vector
    # x . w + b = -1     for neg "

    # opt-obj = min ||w||
    #           max b

    # constrains : yi (xi . w + b) >= 1
    # it's boiled down to : Class (Features . w + b) >= 1,        maximize b and minimize w

    # solving convex opt problems:
    # libsvm : https://www.csie.ntu.edu.tw/~cjlin/libsvm/
    # cvxopt : http://cvxopt.org/examples/index.html
    # https://www.microsoft.com/en-us/research/publication/sequential-minimal-optimization-a-fast-algorithm-for-training-support-vector-machines
    # https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf
    def __init__(self, visualize=True):
        self.w = -99999
        self.b = -99999
        self.max_feature_value = -99999
        self.min_feature_value = -99999

        self.visualization = visualize
        self.colors = {1: 'r', -1: 'g'}
        if visualize:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)
        pass

    def fit(self, data):  # train
        self.data = data
        # { ||w|| : [w,b] }
        opt_dict = {}
        transforms = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
        all_data = []
        for yi in data:
            for featureset in data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        step_sizes = [
            self.max_feature_value * 0.1,
            self.max_feature_value * 0.01,
            self.max_feature_value * 0.001  # expensive
        ]

        b_range_multiple = 5
        b_multiple = 5
        b_range = self.max_feature_value * b_range_multiple

        latest_optimum = self.max_feature_value * 10

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum], dtype=float)
            optimized = False

            while not optimized:

                for b in np.arange(-b_range, b_range, step * b_multiple):

                    for transformation in transforms:
                        w_t = w * transformation
                        found_option = True
                        # problematic issue in the SVM fundamentally fix with SMO
                        # yi (xi . w + b) >= 1
                        for yi in data:
                            for xi in data[yi]:
                                rule_value = yi * (np.dot(xi, w_t) + b)
                                if not rule_value >= 1:
                                    found_option = False
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]

                if w[0] < 0:
                    optimized = True
                    print('Optimizated a step')
                else:
                    # w = [5,5], step =1 --> w = [4,4]
                    w -= step

            norms = sorted([n for n in opt_dict])
            # ||w|| : [w,b]
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step * 2

    def predict(self, features):
        # sign (x.w+b)
        result = np.sign(np.dot(np.array(features), self.w) + self.b)
        if result != 0 and self.visualization:
            self.ax.scatter(features[0], features[1], s=200, marker='*', c=self.colors[result])
        return result

    def visualize(self):
        [[self.ax.scatter(x[0], x[1], s=100, c=self.colors[i]) for x in self.data[i]] for i in self.data]

        # x.w + b
        # v = x.w + b
        # pos-v = 1
        # neg-v = -1
        # decision-boundary = 0

        def hyperplane(x, w, b, v):
            return (-w[0] * x - b + v) / w[1]

        datarange = (self.min_feature_value * 0.9, self.max_feature_value * 1.1)
        hyp_x_min = datarange[0]
        hyp_x_max = datarange[1]

        # Positive
        psv1 = hyperplane(hyp_x_min, self.w, self.b, 1)
        psv2 = hyperplane(hyp_x_max, self.w, self.b, 1)
        self.ax.plot([hyp_x_min, hyp_x_max], [psv1, psv2], c='k')

        # Negative
        nsv1 = hyperplane(hyp_x_min, self.w, self.b, -1)
        nsv2 = hyperplane(hyp_x_max, self.w, self.b, -1)
        self.ax.plot([hyp_x_min, hyp_x_max], [nsv1, nsv2], c='k')

        # Negative
        db1 = hyperplane(hyp_x_min, self.w, self.b, 0)
        db2 = hyperplane(hyp_x_max, self.w, self.b, 0)
        self.ax.plot([hyp_x_min, hyp_x_max], [db1, db2], 'y--')

        plt.show()


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
