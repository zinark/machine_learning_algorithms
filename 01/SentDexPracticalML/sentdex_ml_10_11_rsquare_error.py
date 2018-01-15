from statistics import mean
import numpy as np


# square error

#               SE * y^
# r**2 = 1 - -------------
#               SE * mean|y|

def best_fit_slope_and_intercept(xs, ys):
    m1 = (mean(xs) * mean(ys)) - mean(xs * ys)
    m2 = mean(xs) ** 2 - mean(xs ** 2)
    m = m1 / m2
    b = mean(ys) - m * mean(xs)
    return m, b


def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) ** 2)


def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)


xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

m, b = best_fit_slope_and_intercept(xs, ys)
print m, b

regression_line = [(m * x) + b for x in xs]
r_squared = coefficient_of_determination(ys, regression_line)

print r_squared # sifir olursa daha hatasiz demektir