import math


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
