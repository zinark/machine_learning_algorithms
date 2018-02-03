import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.metrics import r2_score


class Graph(object):
    @staticmethod
    def residual_graph(y, y_pred):
        plt.figure(figsize=(4, 4))
        plt.scatter(y, y_pred - y, s=5, c='k', marker='*')
        plt.bar(y, y_pred - y, color='orange', alpha=0.1)
        plt.title("r2 score %.3f" % r2_score(y, y_pred))
        plt.legend()
        plt.show()

    @classmethod
    def correlation(cls, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError('Data frame!')

        corr_matrix = df.corr()
        corr_matrix[np.abs(corr_matrix) < 0.6] = 0
        sns.heatmap(corr_matrix, center=0., annot=True)
        plt.show()
