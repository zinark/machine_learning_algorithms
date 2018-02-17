from datetime import date, datetime
import pandas as pd
import numpy as np
import scipy.optimize as spo


class PortManager(object):
    def __init__(self, stockQuery, stocks=["BIMAS.E", "TCELL.E", "VESTL.E", "GARAN.E"],
                 start_value=100):
        self.q = stockQuery
        self.stocks = stocks
        self.start_value = start_value
        self.df = self.q.list_stocks(self.stocks, date(2017, 1, 1), date(2017, 12, 30), normalize=True)

    def allocated_value(self, allocs):
        df = self.df * allocs * self.start_value
        assert isinstance(df, pd.DataFrame)
        return df

    def value(self, allocs):
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
        last_value = self.value(allocs).iloc[-1].value
        rf = -1.0 * (last_value ** 1 / 252)
        return float(k * ((self.daily_returns(allocs) - rf).mean() / self.std_daily_returns(allocs)))

    def f(self, allocs):
        result = self.sharpe(allocs)
        # print allocs, result
        # print "{:0.3f}".format(float(result))
        return -1.0 * result

    def constrain_sum(self, inputs):
        return np.sum(inputs) - 1

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
