import numpy as np
from sklearn import svm, model_selection
import pandas as pd

df = pd.read_csv("data/breast-cancer.data")
df.replace('?', -99999, inplace=True)
df.drop(['Id'], 1, inplace=True)

X = np.array(df.drop(['Class'], 1))
Y = np.array(df['Class'])

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2)

clf = svm.SVC()
clf.fit(X_train, Y_train)
acc = clf.score(X_test, Y_test)

example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1]])
prediction = clf.predict(example_measures)
print acc, prediction
