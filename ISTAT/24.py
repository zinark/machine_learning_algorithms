from random import random
import matplotlib.pyplot as plt

from BSE.StatsUtil import StatsUtil


def flip(n):
    l = []
    for i in range(n):
        r = random()
        l.append(1 if r > 0.5 else 0)

    return l

ys = []
for i in range(10000):

    list = flip(4)
    # print "{:10} {:10} {:0.2f} {:0.2f}".format(
    #     sum(list), len(list), StatsUtil.mean(list), StatsUtil.std_deviation(list)
    # )
    ys.append(StatsUtil.mean(list))
    # ys.append(sum(list))

plt.hist (ys, bins=50, align='mid')
plt.show()