import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import random

data_boston = load_boston()

df = pd.DataFrame(data_boston.data, columns=data_boston.feature_names)

X = df.values[:]
y = data_boston.target[:]

from sklearn.preprocessing import StandardScaler

X_std = StandardScaler().fit_transform(X)
y_std = StandardScaler().fit_transform(y.reshape(-1, 1)).flatten()
plt.figure(figsize=(16, 5))


def plot(xlist, ylist, c='green', l='data'):
    plt.grid(ls=':')
    plt.scatter(xlist, ylist, color=c, label=l, marker='x', s=30)
    plt.xlabel("lstat")
    plt.ylabel("target")
    plt.legend()


def gradientDescent(x, y, theta, learning_rate, m, max_iter, debug=False):
    x_transposed = x.transpose()

    for i in range(max_iter):
        if debug:
            print "iteration = ", i+1
            print
            print "\t", "theta"
            print "\t\t=", theta

        y_pred = np.dot(x, theta)
        loss = y_pred - y
        gradient = np.dot(x_transposed, loss) / m

        if debug:
            print "\t", "y_pred = theta . x"
            print "\t\t=", theta, ".", x
            print "\t\t=", y_pred
            print

            print "\t", "loss = x . theta - y"
            print "\t\t=", y_pred, "-", y
            print "\t\t=", loss
            print

            print "\t", "gradient = (x_t . loss) / m"
            print "\t\t=", x_transposed, ".", loss, "/", m
            print "\t\t=", gradient
            print

        # cost = np.sum(loss ** 2) / (2 * m)
        # print("%d | Cost: %f" % (i, cost))

        if debug:
            print "\t", "theta  = theta - learning_rate * gradient"
            print "\t\t=", theta, " - ", learning_rate * gradient
            print "\t\t=", theta - learning_rate * gradient
            print

        theta = theta - learning_rate * gradient
    return theta


# x, y = np.array([[1],[2],[3]]), np.array([5, 4, 7])
x,y = X_std, y_std
m, n = np.shape(x)
max_iter = 100000
learning_rate = 0.0001
theta = np.ones(n)
theta = gradientDescent(x, y, theta, learning_rate, m, max_iter, debug=False)

print "RESULT theta", theta

# plt.subplot(121)
# plot(x, y, 'red', 'actuals')
#
# plt.subplot(122)
# plot(x, x.dot(theta), 'green', 'predictions')
#
# plt.show()
