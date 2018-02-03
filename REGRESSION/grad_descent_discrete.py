import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import random

data_boston = load_boston()

df = pd.DataFrame(data_boston.data, columns=data_boston.feature_names)

X = df[["LSTAT"]].values[:]
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


def gradientDescent(x, y, theta, learning_rate, m, max_iter):
    x_transposed = x.transpose()
    for i in range(max_iter):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        # cost = np.sum(loss ** 2) / (2 * m)
        # print("%d | Cost: %f" % (i, cost))
        gradient = np.dot(x_transposed, loss) / m

        # refresh theta
        theta = theta - learning_rate * gradient
    return theta


x, y = X_std, y_std
m, n = np.shape(x)
max_iter = 50000
learning_rate = 0.0005
theta = np.ones(n)
theta = gradientDescent(x, y, theta, learning_rate, m, max_iter)

print "x", x
print "y", y
print "theta", theta

plt.subplot(121)
plot(x, y, 'red', 'actuals')

plt.subplot(122)
plot(x, x.dot(theta), 'green', 'predictions')

plt.show()
