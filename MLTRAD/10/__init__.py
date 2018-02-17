from datetime import date, datetime
from MLTRAD.StockQuery import StockQuery
from MLTRAD.PortManager import PortManager
from termcolor import colored
import matplotlib.pyplot as plt
import pandas as pd

q = StockQuery("../2013_17.csv")
all_codes = q.list_codes()
main_code = "FBIST.F"
# codes = ["BIMAS.E", "TCELL.E", "VESTL.E", "GARAN.E", "ASYAB.E"]
codes = ['KOMHL.E', 'ANSGR.E', 'ANHYT.E', 'ADANA.E', 'FBIST.F', 'SAFGY.E', 'GLDTR.F', 'IZOCM.E']
#'FBIST.F'
codes = ['ANSGR.E', 'ANHYT.E', 'GLDTR.F', "BIMAS.E", "TCELL.E"]

port = PortManager(q, codes)
# allocations = [1. / len(port.df.columns)] * (len(port.df.columns))

# df_stocks = pd.DataFrame(columns=["stock", "share"])
# for i in range(len(opt_allocs)):
#     df_stocks.loc[i] = [list(port.df.columns)[i], opt_allocs[i]]
# df_stocks.sort_values(by='share', ascending=False, inplace=True)
# print df_stocks
# for i in range(len(df_stocks)):
#     print "{:8} -> {:0.5f}".format(df_stocks.loc[i].stock, df_stocks.loc[i].share)
# choosen = df_stocks[df_stocks["share"] > 0.1]["stock"].tolist()
# print "opt allocations = ", opt_allocs

allocs = [0.16897606, 0.21328357, 0.41532779, 0.11879691, 0.08361567]
opt_allocs, max_val = port.optimize_allocs()
# df = port.daily_returns(allocs)
# df = port.cumulative_returns(allocs)
port.df.plot()
plt.show()
