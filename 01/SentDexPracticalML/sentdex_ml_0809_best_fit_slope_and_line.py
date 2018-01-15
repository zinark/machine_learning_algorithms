from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


def best_fit_slope_and_intercept(xs, ys):
    m1 = (mean(xs) * mean(ys)) - mean(xs * ys)
    m2 = mean(xs) ** 2 - mean(xs ** 2)
    m = m1 / m2
    b = mean(ys) - m * mean(xs)
    return m, b


xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

m, b = best_fit_slope_and_intercept(xs, ys)
print m, b

regression_line = []
for x in xs:
    value = (m * x) + b
    print x, value
    regression_line.append(value)

predict_x = 8
predict_y = m * predict_x + b

style.use('fivethirtyeight')
plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y)
plt.plot(xs, regression_line)
plt.show()

# PEMDAS
# Parantheses
# Exponents
# Multiplication
# Division
# Addition
# Substruction
