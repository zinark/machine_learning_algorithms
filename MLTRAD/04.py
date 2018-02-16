from datetime import datetime, date
import pandas as pd
import numpy as np

import Integration
from MLTRAD.StockQuery import StockQuery
import matplotlib.pyplot as plt

q = StockQuery("2013_17.csv")
codes = ["AKBNK.E", "ULKER.E","BIMAS.E"]

df = q.list_stocks(
    codes,
    date(2017, 1, 1),
    date.today(),
    normalize=False
)

dr = q.daily_returns(df)
cr = q.cumulative_return(df)

x_akbnk = dr[codes[0]]
x_ulker = dr[codes[1]]
x_bimas = dr[codes[2]]

x_akbnk.hist(color='red', bins=30, label=codes[0], alpha=0.3)
x_ulker.hist(color='black', bins=30, label=codes[1], alpha=0.3)
x_bimas.hist(color='blue', bins=30, label=codes[2], alpha=0.3)
plt.legend()
plt.show()

plt.scatter(x_akbnk, x_ulker)
plt.xlabel(codes[0])
plt.ylabel(codes[1])

beta, alpha = np.polyfit(x_akbnk, x_ulker, 1)
plt.plot (x_akbnk, x_akbnk * beta + alpha, color='red')
plt.show()

plt.scatter(x_akbnk, x_bimas)
plt.xlabel(codes[0])
plt.ylabel(codes[2])
beta, alpha = np.polyfit(x_akbnk, x_bimas, 1)
plt.plot (x_akbnk, x_akbnk * beta + alpha, color='red')

plt.show()

