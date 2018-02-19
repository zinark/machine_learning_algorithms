from datetime import date, datetime

import MLTRAD.Predictor
from MLTRAD.StockQuery import StockQuery
from MLTRAD.PortManager import PortManager
from MLTRAD.Predictor import Predictor

from termcolor import colored
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

code = "ISMEN.E"
date_1 = date(2017, 9, 1)
date_2 = date(2017, 11, 30)
q = StockQuery("../2017.csv")
predictor = Predictor(q)
#
df, m = predictor.fit(code, date_1, date_2)
# X = df[target].values.reshape(-1, 1)
# df['PRED'] = predictor.predict(X)
# df.plot(figsize=(3, 3))
# plt.grid(ls=':')
# plt.show()
# m['error'].std()
# m[m['error'] < 0]['error'].sum() + m[m['error'] > 0]['error'].sum()
