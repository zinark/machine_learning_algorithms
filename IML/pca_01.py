from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectKBest, SelectPercentile
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from termcolor import colored

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
blacks = df["B"].values
prices = boston.target

from sklearn.model_selection import train_test_split
# df = df[["ZN", "RM", "PTRATIO", "CRIM"]]
# df.columns = ["square_footage", "rooms", "school_rank", "crime"]
# df = df[["ZN", "RM"]]
# df.columns = ["square_footage", "rooms"]
# df = df[["PTRATIO", "CRIM"]]
# df.columns = ["school_rank", "crime"]
# df = df[["ZN", "RM", "PTRATIO"]]
# df.columns = ["square_footage", "rooms", "school_rank"]
labels = prices
features = df.values

xs, xs_test, ys, ys_test = train_test_split(features, labels, test_size=0.33, random_state=82)


def make_regr(xs, xs_test, ys, ys_test):
    clf = LinearRegression()
    clf.fit(xs, ys)
    print colored("dt local score  => {}".format(clf.score(xs, ys)), 'green', attrs=['bold'])
    print colored("dt global score => {}".format(clf.score(xs_test, ys_test)), 'green', attrs=['bold'])
    print colored("coeffs          => {}".format(clf.coef_))
    # for i in range(len(df.columns)):
    #     n = df.columns[i]
    #     k = clf.coef_[i]
    #     print colored("\t{:10}\t=> {:0.2f}".format(n, k), "yellow", attrs=['bold'])


def make_pca(data):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=5)
    pca.fit(data)
    return pca


pca = make_pca(features)
print colored("(eigen values) explained variance ratio => {}".format(
    ["{:0.3f}".format(x) for x in pca.explained_variance_ratio_]
), color='blue', attrs=['bold'])

for i in range(len(pca.components_)):
    print "component {}. => {}".format(i, pca.components_[i])

xs_reduced = pca.transform(xs)
xs_reduced_test = pca.transform(xs_test)

make_regr(xs, xs_test, ys, ys_test)
make_regr(xs_reduced, xs_reduced_test, ys, ys_test)