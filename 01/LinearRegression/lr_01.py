# http://onlinestatbook.com/2/regression/intro.html

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 2, 1.30, 3.75, 2.25]
})


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


def estimation_error(dataframe):
    error = abs((df['r'] - df['y']))
    exy = (df['x'] * error).sum()
    ex2 = (df['x'] ** 2).sum()
    ey2 = (error ** 2).sum()

    return exy / np.sqrt(ex2 * ey2)

    # # estimation error
    # error_sum = 0
    # total_row = dataframe.count().x
    # for i in range(total_row):
    #     i_r = dataframe.loc[i].r
    #     i_y = dataframe.loc[i].y
    #     error_sum += (i_r - i_y) ** 2
    #
    # return np.sqrt(error_sum / total_row)


df['r'] = create_regression_line(df)

# Plotting
plt.scatter(df['x'], df['y'])
plt.plot(df['x'], df['r'])
plt.show()

print df
print "Error", estimation_error(df)

# Another test
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6],
    'y': [5, 4, 6, 5, 6, 7]
})
df['r'] = create_regression_line(df)
print "Error", estimation_error(df)
