import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(4, 4))
import seaborn as sns

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

boston = load_boston()
y = np.array(boston.target)
df = pd.DataFrame(boston.data, columns=boston.feature_names)

clf = LinearRegression()
x = df.values
clf.fit(x, y)

y_preds = clf.predict(x)

plt.subplot(211)
plt.grid(ls=':')
plt.bar(y_preds, y - y_preds, alpha=0.2, label='pred-error %.2f' % r2_score(y, y_preds))
plt.legend()

# _____________________________________________________________________ StatsModel
import statsmodels.api as sm
X = sm.add_constant(df[['RM', 'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX']])
model = sm.OLS(y, X)
fit_result = model.fit()
print fit_result.summary()
plt.show()