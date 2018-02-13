from datetime import datetime, date
import pandas as pd
import numpy as np

import Integration
from MLTRAD.StockQuery import StockQuery
import matplotlib.pyplot as plt

plt.figure(figsize=(13, 8))

# Integration.Integration.dump_range(filename="stock.csv",
#                                    d1=date(2013, 1, 1),
#                                    d2=date.today())
# q = StockQuery("thisyear.csv")
q = StockQuery("2013_17.csv")
# codes = ["ULKER.E", "BIMAS.E", "TUPRS.E", "VAKBN.E", "YKBNK.E", "AKBNK.E"]
codes = ["AKBNK.E"]

df = q.list_stocks(
    codes,
    date(2017, 1, 1),
    date.today(),
    normalize=False
)


dr = q.daily_returns(df)
dr = q.daily_returns(df)
cr = q.cumulative_return(df)
# print df.head()
# print dr.head()
# print cr.head()
df.columns = ["base"]
df2 = df.join (cr)
df2.columns = ["base", "cr"]
df3 = df2.join(dr)
df3.columns = ["base", "cr", "dr"]
print df3
dr.hist()
plt.show()

