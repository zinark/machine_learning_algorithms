import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)

y = boston.target
f1 = "INDUS"
f2 = "AGE"
X = df[[f1, f2]]

from sklearn.cluster import KMeans
clf = KMeans (n_clusters=7)
clf.fit(X, y)

y_pred = clf.predict(X)

colors = ['red', 'green', 'yellow', 'blue', 'orange', 'black', 'grey']
for i in range(len(X)):
    x1 = X.iloc[i][f1]
    x2 = X.iloc[i][f2]
    ypred = clf.predict([[x1, x2]])[0]

    plt.scatter(x1, x2, s=1, c=colors[ypred])
# plt.scatter(X[f1].values, X[f2].values, s=1)
plt.show()

