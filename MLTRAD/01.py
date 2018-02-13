from datetime import datetime, date
import pandas as pd
import numpy as np

import Integration
from MLTRAD.StockQuery import StockQuery
import matplotlib.pyplot as plt

# Integration.Integration.dump_range(filename="stock.csv",
#                                    d1=date(2013, 1, 1),
#                                    d2=date.today())
# q = StockQuery("thisyear.csv")
q = StockQuery("2013_17.csv")
codes = ["ULKER.E", "BIMAS.E", "TUPRS.E", "VAKBN.E", "YKBNK.E", "AKBNK.E"]
codes = ["BIMAS.E"]

df = q.list_stocks(
    codes,
    date(2017, 1, 1),
    date.today(),
    normalize=False
)
ax = df.plot(fontsize=7, title="plot")
ax.set_xlabel("date")
ax.set_ylabel("price")
plt.legend()

rm, rstd, upper_band, lower_band = q.bollinger_bands(df["BIMAS.E"])
rm.plot(label="rollingmean", ax=ax)
upper_band.plot(ax=ax, color="grey", linewidth=1)
lower_band.plot(ax=ax, color="grey", linewidth=1)
plt.show()
