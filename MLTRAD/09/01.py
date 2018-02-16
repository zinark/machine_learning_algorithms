import scipy.optimize as spo
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = (x - 1.5) ** 2 + 0.5
    print "f({}) = {}".format(x, y)
    return y


def optimize(f, initial=0):
    opt = {
        'disp': True
    }
    min_result = spo.minimize(f, initial, method='SLSQP', options=opt)
    return min_result


result = optimize(f)
print "x    =", result.x
print "min y=", result.fun

xs = np.linspace(0.5, 2.5, 100)
ys = f(xs)

plt.plot(xs, ys, linewidth=1)
plt.scatter(result.x, result.fun)
plt.show()