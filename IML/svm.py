import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=["l", "w", "pl", "pw"])
df["OUT"] = iris.target
X = df[["l", "w"]].values
y = df["OUT"].values

clf = svm.SVC()
clf.fit(X, y)

for x in X:
    y_pred = clf.predict([x])[0]
    print x, y_pred
    plt.scatter(x[0], x[1])
for cls in df["OUT"].unique():
    x_coord = df[df["OUT"] == cls]["l"].values
    y_coord = df[df["OUT"] == cls]["w"].values
    print x_coord
    print y_coord
    plt.scatter(x_coord, y_coord, label=str(cls))
plt.legend()

x_range = np.arange(2.5, 8, 0.01)
y_range = np.arange(0, 8, 0.01)
xx, yy = np.meshgrid(x_range, y_range)
z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
plt.contourf(xx, yy, z, cmap='afmhot', alpha=0.3)

plt.show()
#
# plt.scatter(X[0], X[1], color=clf.predict(X[0], X[1]))
# plt.xlabel("sepal length (cm)")
# plt.ylabel("class")
# plt.show()
