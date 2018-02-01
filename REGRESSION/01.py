import pandas as pd
import numpy as np
import sklearn.datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

iris = sklearn.datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
print df.head()

x = 10 * np.random.rand(100)
y = -5 * x + np.random.rand(100)
X = x.reshape(-1, 1)
model = LinearRegression(fit_intercept=True)
model.fit(X, y)

print model.coef_, model.intercept_

x_fit = np.linspace(-1, 11)
X_fit = x_fit.reshape(-1, 1)
y_fit = model.predict(X_fit)

plt.scatter(x, y)
lbl = 'regression y=%f x + %f'  % (model.coef_[0], model.intercept_)
plt.plot(X_fit, y_fit, label=lbl, color='red')
plt.legend()
plt.show()
