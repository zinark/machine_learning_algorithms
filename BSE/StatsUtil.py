import math
class StatsUtil():

    @staticmethod
    def mean(X):
        assert isinstance(X, type([]))
        return sum(X) / len(X)

    @staticmethod
    def median(X, avg=True):
        assert isinstance(X, type([]))
        X = sorted(X)
        length = len(X)
        middle = length / 2
        if not avg:
            return X[(length - 1) / 2]

        if length % 2 == 0:
            return (X[middle] + X[middle - 1]) / 2.
        else:
            return X[middle]

    @staticmethod
    def mode(X):
        assert isinstance(X, type([]))
        frequency = []
        for i in sorted(set(X)):
            frequency.append([i, (X.count(i))])
        return sorted(frequency, key=lambda x: x[1])[-1][0]

    @staticmethod
    def variance(X):
        m = StatsUtil.mean(X)
        N = len(X)
        return StatsUtil.mean([(x - m) ** 2 for x in X])

    @staticmethod
    def std_deviation(X):
        return math.sqrt(StatsUtil.variance(X))
