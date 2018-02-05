import sys
from sklearn.datasets import load_boston

sys.path.append("..")
import pandas as pd
from sklearn.preprocessing import StandardScaler

from BSE.Util import Util

data_boston = load_boston()
df = pd.DataFrame(data_boston.data, columns=data_boston.feature_names)
X_std = StandardScaler().fit_transform(df.values)
y_std = StandardScaler().fit_transform(data_boston.target.reshape(-1, 1)).flatten()
theta, history = Util.grad_descent(X_std, y_std)
print "RESULT theta", theta
