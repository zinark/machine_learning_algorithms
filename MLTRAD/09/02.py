import scipy.optimize as spo
import matplotlib.pyplot as plt
import numpy as np


def error(line, data):
    """
    :param line: (C0, C1)
    :param data: 2d array (x,y)
    :return: error
    """
    xs = data[:, 0]
    ys = data[:, 1]

    c0 = line[0]
    c1 = line[1]

    y_pred = c0 * xs + c1

    err = np.sum((ys - y_pred) ** 2)

    return err


def optimize(f, data, initial=0):
    opt = {
        'disp': True
    }
    min_result = spo.minimize(f, initial, args=(data,), method='SLSQP', options=opt)
    return min_result


data = np.array([
    [1, 2],
    [2, 1],
    [3, 1.7],
    [4, 3],
    [5, 2.3],
    [6, 2.5],
])

print error((0, 0), data)
result = optimize(error, data, initial=(0, 0))


print "x    =", result.x
print "min y=", result.fun

xs = data[:, 0]
ys = data[:, 1]

ypred = result.x[0] * xs + result.x[1]

plt.scatter(xs, ys, linewidth=1)
plt.plot(xs, ypred, linewidth=2)

plt.show()
