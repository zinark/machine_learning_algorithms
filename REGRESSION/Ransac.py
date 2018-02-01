import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("boston.csv")
X = df['lstat'].values.reshape(-1, 1)
y = df['medv'].values

from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import LinearRegression

clf = RANSACRegressor()
clf2 = LinearRegression()
clf.fit(X, y)
clf2.fit(X,y)

inlier_mask = clf.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

line_x = np.arange(np.min(X), np.max(X), 0.1)
line_y = clf.predict(line_x.reshape(-1,1))
line_y2 = clf2.predict(line_x.reshape(-1,1))

sns.set_style(style='darkgrid')
plt.figure(figsize=(12, 10))

plt.scatter(X[inlier_mask], y[inlier_mask], c='blue', marker='o', label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask], c='red', marker='x', label='Outliers')
plt.plot (line_x, line_y, color='green', label='ransac')
plt.plot (line_x, line_y2, color='red', label='regression')

plt.xlabel("low quality neighbor")
plt.ylabel("price")
plt.legend()
plt.show()