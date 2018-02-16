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
# df = df[["ZN", "RM", "PTRATIO", "CRIM"]]
# df.columns = ["square_footage", "rooms", "school_rank", "crime"]
prices = boston.target

from sklearn.model_selection import train_test_split

labels = prices
features = df.values

xs, xs_test, ys, ys_test = train_test_split(features, labels, test_size=0.33, random_state=82)

clf = LinearRegression()
clf.fit(xs, ys)
print colored("dt local score  => {}".format(clf.score(xs, ys)), 'green', attrs=['bold'])
print colored("dt global score => {}".format(clf.score(xs_test, ys_test)), 'green', attrs=['bold'])
print colored("coefs names     => {}".format(df.columns.tolist()), 'green', attrs=['bold'])
print colored("coefs values    => {}".format(clf.coef_), 'green', attrs=['bold'])

from sklearn.feature_selection import SelectPercentile, chi2, f_oneway, f_classif, f_regression, SelectKBest

selector = SelectPercentile(score_func=f_regression, percentile=10)
selector = SelectKBest(score_func=f_regression, k=5)
selector.fit(xs, ys)
print colored(selector.scores_, "blue", attrs=['reverse'])
xs = selector.transform(xs)
xs_test = selector.transform(xs_test)
clf = LinearRegression()
clf.fit(xs, ys)
print colored("dt local score  => {}".format(clf.score(xs, ys)), 'green', attrs=['bold'])
print colored("dt global score => {}".format(clf.score(xs_test, ys_test)), 'green', attrs=['bold'])
print colored("coefs values    => {}".format(clf.coef_), 'green', attrs=['bold'])
