import numpy as np


def g_1():
    from sklearn.model_selection import train_test_split, KFold

    X = np.arange(1, 100, 10)
    y = np.arange(100, 200, 10)

    print len(X), X
    print len(y), y

    kf = KFold(4, shuffle=True)

    for train_i, test_i in kf.split(X):
        print "Train", train_i
        print "Test", test_i


# _________________________

from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV

iris = load_iris()

fitter = SVC()
clf = GridSearchCV(fitter,param_grid = {
    'kernel': ['rbf', 'linear', 'poly', 'sigmoid'],
    'C': [1, 10, 100, 1000]
}, n_jobs=10, cv=5)
clf.fit(iris.data, iris.target)
print clf.best_params_
print clf.best_score_
print clf.best_index_