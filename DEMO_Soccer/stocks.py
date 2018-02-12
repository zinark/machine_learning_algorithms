import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
from Integration import Integration
plt.figure(figsize=(14, 7))
#Kozal.e tupras.e sasa.e
# code = "KOZAL.E"
code = "ADBGR.E"
# Integration.dump_range("test.csv", datetime.date (2017, 12, 1), datetime.date.today())
# Integration.dump_range("train.csv", datetime.date (2012, 1, 1), datetime.date (2017, 12, 1))
df = Integration("train.csv").get_stock(code)
df_test = Integration("test.csv").get_stock(code)
print df

alpha = 30

xs = []
ys = []
pick_ys = []
pick_xs = []

for i in range(len(df)):
    no = df.iloc[i]["no"]
    diff = df.iloc[i]["diff"]
    diff_prev = 2018715

    if i >= alpha:
        diff_prev = df.iloc[i - 1]["diff"]
        rlist=[]
        for n in range(i - alpha, i):
            rlist.append (df.iloc[n]["diff"])
        pick_xs.append(rlist)
    else:
        pick_xs.append([-9999] * alpha)

    xs.append(no)
    ys.append(diff)

    if diff > diff_prev:
        pick_ys.append(1)
    if diff == diff_prev:
        pick_ys.append(0)
    if diff < diff_prev:
        pick_ys.append(-1)

from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier

np.random.seed(8219)
clf_mlp = MLPClassifier(
                    max_iter=2000,
                    # learning_rate='adaptive',
                    hidden_layer_sizes=(1000, ),
                    solver='adam',
                    activation='relu')

clf_tree = RandomForestClassifier(n_estimators=100, min_samples_split=4)


# clf = AdaBoostClassifier (random_state=1, n_estimators=1000, learning_rate=.01)
clf = BaggingClassifier (base_estimator=clf_mlp,
                         n_estimators=11)

X = np.array(pick_xs)
Y = np.array(pick_ys)
clf.fit(X, Y)


plt.subplot(211)
plt.plot(xs, ys, linewidth=.3)
plt.plot(xs, pick_ys, color='orange', linewidth=0.7)
plt.title(type(clf).__name__)
plt.grid(ls=":")

xs_test = []
ys_test = []
xs_pick_test = []
ys_pick_test = []
for i in range(len(df_test)):
    no = df_test.iloc[i]["no"]
    diff = df_test.iloc[i]["diff"]
    diff_prev = 2018715
    if i >= alpha:
        diff_prev = df_test.iloc[i - 1]["diff"]
        rlist=[]
        for n in range(i - alpha, i):
            rlist.append (df_test.iloc[n]["diff"])
        xs_pick_test.append(rlist)
    else:
        xs_pick_test.append([-9999] * alpha)

    xs_test.append(no)
    ys_test.append(diff)

    if diff > diff_prev:
        ys_pick_test.append(1)
    if diff == diff_prev:
        ys_pick_test.append(0)
    if diff < diff_prev:
        ys_pick_test.append(-1)

plt.subplot(212)
plt.plot(xs_test, ys_test, linewidth=.3)
plt.plot(xs_test, ys_pick_test, linewidth=2)

y_pred = clf.predict(xs_pick_test)
plt.scatter(xs_test, y_pred, c='red')


accuracy = 0.
leny = len(ys_pick_test) - alpha
for i in range(leny):
    if ys_pick_test[alpha + i] == y_pred[alpha + i]:
        accuracy+=1
accuracy = accuracy/leny
print "%", accuracy

plt.title("acc {0:0.3f}".format(accuracy))
plt.grid(ls=":")
plt.suptitle (str(code))
plt.show()
