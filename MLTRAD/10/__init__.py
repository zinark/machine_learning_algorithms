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
date_2 = date(2018, 1, 1)
port = PortManager(q, code_list,
                   date_1=date_1,
                   date_2=date_2
                   )
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


df = port.print_opt()
print df
