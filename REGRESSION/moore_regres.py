import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("moore.csv", delimiter="\t", header=None)
df.columns = ["model", "units", "year", "company", "x2", "x3"]
df = df[["year", "units"]]
# df["year"] = df["year"].asof(int)
# df["units"] = df["units"].asof(int)

df["year"] = df["year"].apply(lambda x: int(x))
df["units"] = df["units"].apply(lambda x: x.replace(",", "").replace("~", "").replace("cca", "").split("[")[0])
df["units"] = df["units"].apply(lambda x: int(x))
X = np.array(df["year"].values)
Y = np.array(df["units"].values)

denom = X.dot(X) - X.mean() * X.sum()
a = (X.dot(Y) - Y.mean() * X.sum()) / denom
b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denom

y_pred = a * X + b

plt.scatter(X, Y)
plt.plot(X, y_pred)
plt.show()


residual = Y - y_pred
total = Y - Y.mean()
r2_score = 1 - residual.dot(residual) / total.dot(total)
