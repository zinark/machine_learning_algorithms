import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from BSE.Util import Util

df = pd.read_csv("moore.csv", delimiter="\t", header=None)
df.columns = ["model", "units", "year", "company", "x2", "x3"]
df = df[["year", "units"]]

df["year"] = df["year"].apply(lambda x: int(x))
df["units"] = df["units"].apply(lambda x: x.replace(",", "").replace("~", "").replace("cca", "").split("[")[0])
df["units"] = df["units"].apply(lambda x: int(x))
X = np.array(df["year"].values)
Y = np.array(df["units"].values)

a, b, r2_score = Util.linear_regression_on_vectors(X, Y)
y_pred = a * X + b

plt.scatter(X, Y)
plt.plot(X, y_pred)
plt.show()
