import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
from Integration import Integration

# df = Integration.get_stock("2017.csv", code="ADEL.E")
df = Integration.get_stock("2017.csv", code="ADANA.E")
print df

xs = []
ys = []
picks = []

for i in range(1, len(df)):

    no = df.iloc[i]["no"]
    diff = df.iloc[i]["diff"]
    diff_prev = df.iloc[i - 1]["diff"]

    xs.append(no)
    ys.append(diff)
    if diff > diff_prev:
        picks.append(1)
    else:
        picks.append(0)

plt.plot(xs, ys)
plt.plot(xs, picks, color='red')
plt.grid(ls=":")
plt.show()
