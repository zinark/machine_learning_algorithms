import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("boston.csv")
print df.head()

# sns.pairplot(df[["zn", "indus", "nox", "rm"]], size=3)
# sns.pairplot(df[["ptratio", "b", "lstat", "medv"]], size=1.5)
# plt.show()
pd.options.display.float_format = '{:,.1f}'.format
plt.figure(figsize=(12,8))
d = df[["crim", "zn", "indus", "chas", "medv"]]
d["corr"] = -1 * df["indus"] + df["zn"]
sns.heatmap(d.corr(), annot=True, linewidths=.1, center=0)
plt.show()