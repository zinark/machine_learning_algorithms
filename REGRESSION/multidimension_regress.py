import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from BSE.Util import Util

df = pd.read_csv("2d.csv", header=None)
X = np.array(df[[0, 1]].values)
y = np.array(df[2].values)

w, r2 = Util.linear_regression_on_matrices(X, y)
ypred = X.dot(w)

fig = plt.figure(figsize=(15, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(X[:, 0], X[:, 1], y, label='inputs', color='black', s=15, marker='x')
# ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
ax1.view_init(45, 0)
ax1.plot(sorted(X[:, 0]), sorted(X[:, 1]), sorted(ypred), label='prediction', color='red', alpha=0.2)
plt.xlabel("x1")
plt.ylabel("x2")

ax1 = fig.add_subplot(122, projection='3d')
ax1.scatter(X[:, 0], X[:, 1], y, label='inputs', color='black', s=15, marker='x')
# ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
ax1.view_init(45, -90)
ax1.plot(sorted(X[:, 0]), sorted(X[:, 1]), sorted(ypred), label='prediction', color='red', alpha=0.2)
plt.xlabel("x1")
plt.ylabel("x2")

plt.show()
