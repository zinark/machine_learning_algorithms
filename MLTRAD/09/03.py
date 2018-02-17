import scipy.optimize as spo
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 50 + 60 * x - 5 * x ** 2 - 10 * x ** 3 + 1.5 * x ** 4 + np.random.randn()*100


def error(C, xs, ys):
    y_pred = np.polyval(C, xs)
    err = np.sum((ys - y_pred) ** 2)
    return err


def optimize(f, xs, ys, initial=0):
    opt = {
        'disp': True
    }
    min_result = spo.minimize(f, initial, args=(xs, ys,), method='SLSQP', options=opt)
    return min_result


xs = np.linspace(-3, 3, 20)
ys = f(xs)

c = np.ones(5)
print (error(c, xs, ys))
result = optimize(error, xs, ys, initial=c)

print "x    =", result.x
print "min y=", result.fun

y_pred = np.polyval(result.x, xs)

plt.scatter(xs, ys, linewidth=1)
plt.plot(xs, y_pred, linewidth=2)

plt.show()
