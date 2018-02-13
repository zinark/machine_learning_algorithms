from datetime import datetime, date
import pandas as pd
import numpy as np

import Integration
from MLTRAD.StockQuery import StockQuery
import matplotlib.pyplot as plt

q = StockQuery("2013_17.csv")
codes = ["AKBNK.E", "ULKER.E"]

df = q.list_stocks(
    codes,
    date(2017, 1, 1),
    date.today(),
    normalize=False
)

dr = q.daily_returns(df)
cr = q.cumulative_return(df)

dr[codes[0]].hist(color='red', bins=30, label=codes[0], alpha=0.3)
dr[codes[1]].hist(color='black', bins=30, label=codes[1], alpha=0.3)
plt.legend()
plt.show()

