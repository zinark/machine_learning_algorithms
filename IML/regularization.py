# min (SSE + phi . |features|)
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso

xs = [
    [1, 10],
    [2, 10],
    [3, 10],
    [4, 10]
]
ys = [10, 20, 30, 40]

xs_test = [
    [5, 9],
    [6, 12]
]

ys_test = [50, 60]

clf = LinearRegression()
clf.fit(xs, ys)
print "regression score=", clf.score(xs_test, ys_test), clf.coef_

lasso = Lasso()
lasso.fit(xs, ys)
print "lasso score=", lasso.score(xs_test, ys_test), lasso.coef_
