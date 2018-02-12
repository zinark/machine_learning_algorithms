import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
from Integration import Integration
plt.figure(figsize=(20, 8))
#Kozal.e tupras.e sasa.e
# code = "KOZAL.E"
code = "SASA.E"
df = Integration.get_stock("2017.csv", code=code)
df_test = Integration.get_stock("2018.csv", code=code)
print df

alpha = 7

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

clf = MLPClassifier(hidden_layer_sizes=(1000, 1000), solver='lbfgs', activation='relu')
X = np.array(pick_xs)
Y = np.array(pick_ys)
clf.fit(X, Y)


plt.subplot(211)
plt.plot(xs, ys, linewidth=.3)
plt.scatter(xs, pick_ys, color='red', s=5)
plt.title("tr")
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
plt.plot(xs_test, ys_pick_test, linewidth=.3)

y_pred = clf.predict(xs_pick_test)
plt.scatter(xs_test, y_pred, c='red')

plt.title("ts")
plt.grid(ls=":")
plt.show()

accuracy = 0.
leny = len(ys_pick_test)
for i in range(leny):
    if ys_pick_test[i] == y_pred[i]:
        accuracy+=1

print "%", accuracy/leny