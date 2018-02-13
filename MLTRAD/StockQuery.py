from datetime import datetime, date
import pandas as pd
from Integration import Integration
import matplotlib.pyplot as plt


class StockQuery(object):
    def __init__(self, file):
        src = Integration(file)
        self.q = src.get_all()

    def daily_returns(self, df):
        dr = (df / df.shift(1)) - 1
        dr.ix[0, :] = 0
        return dr

    def cumulative_return(self, df):
        return (df / df.ix[0, :]) - 1

    def list_stocks(self, codes=["ULKER.E", "AKBNK.E", "BIMAS.E"], date1=None, date2=None, normalize=False):
        date_1 = date(2018, 1, 1)
        date_2 = date.today()
        if date1 is not None and date2 is not None:
            date_1 = date1
            date_2 = date2

        dates = pd.date_range(date_1, date_2)
        df = pd.DataFrame(index=dates)
        q = self.q
        for code in codes:
            df_temp = q[q["code"] == code].set_index("date").drop("code", axis=1)[["close"]]
            df_temp.columns = [code]
            df = df.join(df_temp, how='inner')
        if normalize:
            df = df / df.ix[0, :]

        return df

    def list_codes(self):
        return self.q["code"].unique().tolist()

    def bollinger_bands(self, X):
        rollingmean = X.rolling(10).mean()
        rollingstd = X.rolling(10).std()

        return rollingmean, rollingstd, rollingmean - rollingstd * 2, rollingmean + rollingstd * 2
