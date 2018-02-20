# coding=utf-8
# 1138
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from MLTRAD.StockQuery import StockQuery
from datetime import date

search_query = u'SASA hisse'
stock_symbol = 'SASA.E'
d1 = date(2017, 1, 1)
d2 = date(2017, 11, 30)

t = TrendReq(hl='tr-TR', tz=360)
t.build_payload([search_query], timeframe="{} {}".format(str(d1), str(d2)),
                geo='TR')
trends = t.interest_over_time()
trends.columns = ["trend", "ispartial"]
# trends["trend"] = (trends["trend"] + 1.0)

# trends["trend"] = trends["trend"].shift(7)
q = StockQuery('2013_17.csv')
stocks = q.list_stocks([stock_symbol], d1, d2, normalize=True)
stocks.columns = ["dr"]

trends["trend"] = (trends["trend"] / (trends["trend"].max())) / 10.
df = stocks.join(trends, how='left')
df["dr"] = q.daily_returns(df[["dr"]])

df = df[["dr", "trend"]]
df = df.fillna(0)
# total_feature = 7
# # historic
# for i in range(1, total_feature):
#     df["dr_{}".format(i)] = df["dr"].shift(-i)

next_week = 7
df['d'] = df['dr'].shift(-next_week)
df = df[:-next_week]

df['y'] = df['d'].apply(lambda x: 1 if x > 0 else -1 if x < 0 else 0)

df[["dr", "trend"]].plot()
plt.show()

from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
clf = MLPClassifier(hidden_layer_sizes=(1000, 100), activation='relu')
cols = ["dr", "trend"]
# for i in range(1, total_feature):
#     cols.append("dr_{}".format(i))

features = df[cols]
labels = df["y"]
f_train, f_test, l_train, l_test = train_test_split(features, labels, test_size=0.1, random_state=34)
clf.fit(f_train, l_train)

print clf.score(f_test, l_test)
#confusion_matrix()