from datetime import date, datetime
import pandas as pd
import numpy as np
import scipy.optimize as spo
from StockQuery import StockQuery
import matplotlib.pyplot as plt
from termcolor import colored

class PortManager(object):
    def __init__(self, stockQuery, stocks=["BIMAS.E", "TCELL.E", "VESTL.E", "GARAN.E"],
                 start_value=100, date_1=date(2017, 1, 1), date_2=date(2018, 1, 1)):
        assert isinstance(stockQuery, StockQuery)
        self.q = stockQuery
        self.date_1 = date_1
        self.date_2 = date_2
        self.stocks = stocks
        self.start_value = start_value
        self.df = self.q.list_stocks(self.stocks, date_1, date_2, normalize=True)

    def allocated_value(self, allocs):
        df = self.df * allocs * self.start_value
        assert isinstance(df, pd.DataFrame)
        return df

    def value(self, allocs):
        if len(self.df.columns) < 1:
            return None

        df = self.df * allocs * self.start_value
        df = pd.DataFrame(df.sum(axis=1))
        df.columns = ["value"]
        assert isinstance(df, pd.DataFrame)
        return df

    def daily_returns(self, allocs):
        return self.q.daily_returns(self.value(allocs))[1:]

    def cumulative_returns(self, allocs):
        port_value = self.value(allocs)
        return (port_value.iloc[-1]["value"] / port_value.iloc[0]["value"]) - 1.

    def average_daily_returns(self, allocs):
        return self.daily_returns(allocs).mean()

    def std_daily_returns(self, allocs):
        return self.daily_returns(allocs).std()

    def sharpe(self, allocs):
        k = np.sqrt(252)
        values = self.value(allocs)
        if values is None:
            return 0
        last_value = values.iloc[-1].value
        rf = -1.0 * (last_value ** 1 / 252)
        return float(k * ((self.daily_returns(allocs) - rf).mean() / self.std_daily_returns(allocs)))

    def f(self, allocs):
        result = self.sharpe(allocs)
        # result = self.cumulative_returns(allocs)
        # print allocs, result
        # print "{:0.3f}".format(float(result))
        return -1.0 * result

    def constrain_sum(self, inputs):
        return np.sum(inputs) - 1

    def print_opt(self):
        x = self.optimize_allocs()[0]
        self.x_ = x
        cols = self.df.columns.tolist()
        print "cols=", cols
        print "x=", x
        for i in range(len(x)):
            print "{:10} -> {:0.4f}".format(cols[i], x[i])

        return self.value(x)

    def optimize_allocs(self):
        features = len(self.df.columns)
        bnds = features * [(0., 1.)]
        sum_constraints = ({'type': 'eq', "fun": self.constrain_sum})
        allocations = [1. / features] * (features)
        result = spo.minimize(self.f,
                              allocations,
                              method='SLSQP',
                              options={'disp': True},
                              bounds=bnds,
                              constraints=sum_constraints)

        return result.x, -result.fun

    def find(self, n):
        q = self.q
        all_codes = q.list_codes()
        total = len(all_codes)
        print colored("n_codes={}".format(n), "green", attrs=['reverse'])
        print colored("n_features={}".format(total), "blue", attrs=['reverse'])

        r = pd.DataFrame(columns=["code", "sharpe"])
        for i in range(total):
            code = all_codes[i]
            sharpe = PortManager(q, [code], self.start_value, self.date_1, self.date_2).sharpe([1])
            print i, code, sharpe
            r.loc[i] = [code, sharpe]

        return r

    def predict(self, x_input):
        return self.clf.predict(x_input)
