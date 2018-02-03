from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Graph import Graph
from Util import Util

boston = load_boston()
df = pd.DataFrame(data=boston.data, columns=boston.feature_names)
y = boston.target


def measure_regression():
    corr_matrix = df.corr()
    corr_matrix[np.abs(corr_matrix) < 0.6] = 0
    plt.figure(figsize=(4, 4))
    sns.heatmap(corr_matrix, annot=True, center=0)
    plt.show()
    eigenvalues, eigenvectors = np.linalg.eig(df.corr())
    least_effecteds = pd.Series(eigenvalues).sort_values()
    most_effectors_data = np.abs(pd.Series(eigenvectors[:, 8])).sort_values(ascending=False)
    most_effectors = most_effectors_data.keys().tolist()
    # multi colinearity
    most_effector_columns = df.columns[most_effectors[:3]].tolist()
    print most_effector_columns
    # most coefficients
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(df.values, y)
    d = list(zip(model.coef_, df.columns))
    result = pd.DataFrame(d, columns=['coefficient', 'name']).set_index('name')
    result = np.abs(result).sort_values(by='coefficient', ascending=False)
    print result

print Util.top_coefficiants(df, y)