# http://onlinestatbook.com/2/regression/intro.html

import pandas as pd
import numpy as np
import random

import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x': range(1, 7),
    'y': [5, 4, 6, 5, 6, 7]
})


def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    xs = range(hm)
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)

        if correlation:
            val += step
        else:
            val -= step

    return np.array(xs), np.array(ys)


def create_regression_line(dataframe):
    # MX is the mean of X, MY is the mean of Y, sX is the standard deviation of X, sY
    # is the standard deviation of Y, and r is
    # the correlation between X and Y.

    xseries = dataframe['x']
    yseries = dataframe['y']

    mx = np.mean(xseries)
    my = np.mean(yseries)
    sx = np.std(xseries)
    sy = np.std(yseries)
    r = np.corrcoef(xseries, yseries)[0][1]
    print "Mx = ", mx
    print "My = ", my
    print "Sx =", sx
    print "Sy =", sy
    print "r =", r
    slope = r * sy / sx
    intercept = my - slope * mx
    print "b (slope) = ", slope
    print "A (intercept) = ", intercept

    # Generate regressionline
    return [(slope * x) + intercept for x in xseries]


def estimation_error(df):
    ymean = df['y'].mean()
    dist_to_regression = df['y'] - df['r']
    dist_to_mean = df['y'] - ymean
    e1 = np.sum(dist_to_regression ** 2)
    e2 = np.sum(dist_to_mean ** 2)
    return 1 - (e1 / e2)


xlist, ylist = create_dataset(30, 5, 1, True)
df = pd.DataFrame({
    'x': xlist,
    'y': ylist
})
df['r'] = create_regression_line(df)

# Plotting
print df
print estimation_error(df)

plt.scatter(df['x'], df['y'])
plt.plot(df['x'], df['r'])
plt.show()
