import numpy as np
from timeit import timeit


def dot_product(a, b):
    summation = 0.
    for i, j in zip(a, b):
        summation += i * j
    return summation


print "time1:", timeit(lambda: dot_product(np.random.rand(100), np.random.rand(100)))
print "time2:", timeit(lambda: np.dot(np.random.rand(100), np.random.rand(100)))
