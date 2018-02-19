from datetime import date, datetime
from MLTRAD.StockQuery import StockQuery
from MLTRAD.PortManager import PortManager
from termcolor import colored
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

q = StockQuery("../2013_17.csv")
all_codes = q.list_codes()
main_code = "FBIST.F"
# codes = ["BIMAS.E", "TCELL.E", "VESTL.E", "GARAN.E", "ASYAB.E"]
codes = ['KOMHL.E', 'ANSGR.E', 'ANHYT.E', 'ADANA.E', 'FBIST.F', 'SAFGY.E', 'GLDTR.F', 'IZOCM.E']
codes = ['KOMHL.E', 'ANSGR.E', 'ANHYT.E', 'GLDTR.F']

code_list = [
    # "YESIL.E",
    "YATAS.E",
    # "FBIST.F",
    "GLDTR.F", "GOLDP.F", "ANSGR.E",
    "ANHYT.E",
    "USDTR.F",
    "ULUSE.E",
    "HEKTS.E",
    # "IST30.F",
    # "ISY30.F",
    "DJIST.F",
    "FROTO.E",
    "ADANA.E",
    "TBORG.E",
    "ISMEN.E",
    "MAVI.E",
    "IZFAS.E",
    "THYAO.E",
]

# 'FBIST.F'
# codes = ['ANSGR.E', 'ANHYT.E', 'GLDTR.F', "BIMAS.E", "TCELL.E"]

date_1 = date(2017, 1, 1)
date_2 = date(2017, 9, 1)

portfolio = PortManager(q, code_list,
                        date_1=date_1,
                        date_2=date_2
                        )

target = "ISMEN.E"
portfolio.fit(target)
df = q.list_stocks([target], date_1, date_2, normalize=True)
df['PRED'] = portfolio.predict(df[target].values.reshape(-1, 1))
# df['PRED'] = df['PRED'].fillna(1)
df.plot(figsize=(24,12))
plt.grid(ls=':')
plt.show()
# df = port.find(1)
# print df.sort_values(by='sharpe', ascending=False)
# allocs, max_val = port.optimize_allocs()
# print allocs
# print port.value(allocs)

# t = pd.read_csv("candidates.csv")
# codes = t["code"][0:5].values.tolist()
# df = q.list_stocks(code_list, date_1, date_2, normalize=True)
# df.plot()
# plt.show()
#
#
# df = port.print_opt()
# print df
