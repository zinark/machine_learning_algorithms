from datetime import datetime, date
import pandas as pd

from MLTRAD.StockQuery import StockQuery
import matplotlib.pyplot as plt

# Integration.dump_range("stock.csv", datetime.date(2018, 1, 1), date.today())
# q = StockQuery("2013_17.csv")
q = StockQuery("2017.csv")
df = q.list_stocks(
    ["ULKER.E", "AKBNK.E", "BIMAS.E"],
    date(2017, 1, 1),
    date.today(),
    normalize=True
)
ax = df.plot(fontsize=7, title="plot")
ax.set_xlabel("date")
ax.set_ylabel("price")
plt.legend()
plt.show()