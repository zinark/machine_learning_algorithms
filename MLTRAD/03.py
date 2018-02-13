from datetime import datetime, date
import pandas as pd
import numpy as np

import Integration
from MLTRAD.StockQuery import StockQuery
import matplotlib.pyplot as plt

plt.figure(figsize=(13, 8))

q = StockQuery("2013_17.csv")
codes = ["AKBNK.E"]
# codes = ["AKBNK.E", "ULKER.E"]

df = q.list_stocks(
    codes,
    date(2017, 1, 1),
    date.today(),
    normalize=False
)


dr = q.daily_returns(df)
cr = q.cumulative_return(df)
dr.hist(bins=50)
plt.axvline(dr["AKBNK.E"].mean(), color='black', linewidth=0.5, linestyle='dashed')
plt.axvline(dr["AKBNK.E"].std(), color='r', linewidth=0.2, linestyle='dashed')
plt.axvline(-dr["AKBNK.E"].std(), color='r', linewidth=0.2, linestyle='dashed')
print "k=", dr["AKBNK.E"].kurtosis()
plt.show()