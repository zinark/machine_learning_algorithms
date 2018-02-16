import scipy.optimize as spo


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

