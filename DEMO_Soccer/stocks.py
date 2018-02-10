import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import urllib, json
import datetime

url = "https://www.doviz.com/api/v1/stocks/all/latest"
response = urllib.urlopen(url)
r = response.readlines()[0]
print r
fname = "{0}-{1}-{2}.json".format(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
with open(fname, "w") as f:
    f.write(r)
    f.write("\n")
    f.flush()


df = pd.read_json("2018-2-11.json")
df = df.head(10)
df["d"] = - df["previous_second_seance_closing"] + df["previous_first_seance_closing"]
#
# clf = LinearRegression()
# from sklearn.cross_validation import train_test_split
#
# x = df[["previous_first_seance_closing", "previous_second_seance_closing", "profit"]]
# y = df["d"]
#
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
#
# clf.fit(X_train, y_train)
# print "score", clf.score(X_test, y_test)
# # plt.plot(x, clf.predict(x))
#
# plt.scatter(df["name"], df["d"])
# plt.show()
