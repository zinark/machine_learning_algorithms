import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv ("boston.csv")
print df.head ()

input_x = "lstat"
X = df[input_x].values.reshape (-1, 1)
y = df["medv"]

from sklearn.linear_model import LinearRegression
clf = LinearRegression ()
clf.fit (X, y)

print clf.coef_, clf.intercept_

sns.regplot(X,y)
plt.xlabel("% lower status of population")
plt.ylabel("median value of homes in $1000's")
plt.show()

sns.jointplot(x=input_x, y='medv', data=df, kind='reg', size=10)
plt.xlabel("% lower status of population")
plt.ylabel("median value of homes in $1000's")
plt.show()

