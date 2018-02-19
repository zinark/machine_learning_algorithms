import MLTRAD.StockQuery
from termcolor import colored
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.optimize as spo


class Predictor(object):

    def __init__(self, stockQuery):
        assert isinstance(stockQuery, MLTRAD.StockQuery.StockQuery)
        self.q = stockQuery
        self.clf = None

    def fit (self, code, date_1, date_2):
        df = self.q.list_stocks([code], date_1, date_2, normalize=True)
        df = df[[code]] * 1000
        shift_distance = 5
        df_x = df[:-shift_distance]
        df_x.columns = ['x']
        df_y = df.shift(shift_distance)[shift_distance:]
        df_y.columns = ['y']
        m = df_x.join(df_y)[shift_distance:]

        from sklearn.tree import DecisionTreeRegressor
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split

        X = m[['x']]
        y = m[['y']]
        x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=82)
        # clf = DecisionTreeRegressor(min_samples_leaf=2, random_state=82)
        clf = DecisionTreeRegressor()
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        print colored("score={}".format(clf.score(x_test, y_test)), "red", attrs=['reverse'])
        y_all = clf.predict(X)
        m['pred'] = y_all
        m['error'] = m['y'] - m['pred']
        m.plot()
        plt.show()
        self.clf = clf
        return df, m

    def predict(self, x_input):
        return self.clf.predict(x_input)
