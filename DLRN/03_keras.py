import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor

df = pd.read_json('wages.json')
assert isinstance(df, pd.DataFrame)


def eda():
    print df.describe()
    df.hist()
    plt.show()
    print df.kurtosis()
    corr = df.corr()
    corr[np.abs(corr) < 0.3] = 0
    plt.imshow(corr, cmap='Blues')
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.colorbar()
    plt.show()


import keras
from keras.layers import Dense
from keras.models import Sequential

p_cols = [u'age',
          u'construction',
          u'education_yrs',
          u'experience_yrs',
          u'female',
          u'manufacturing',
          u'marr',
          u'south',
          u'union']
n_cols = len(p_cols)

X = df[p_cols].values
y = df['wage_per_hour'].ravel()

model = Sequential()
model.add(Dense(1000, activation='relu', input_shape=(n_cols,)))
model.add(Dense(900, activation='relu'))
model.add(Dense(800, activation='relu'))
model.add(Dense(700, activation='relu'))
model.add(Dense(600, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X, y, epochs=5, validation_split=0.1)
y_pred = model.predict(X).ravel()
print 'dl score=', mean_squared_error(y_pred, y)

clf = DecisionTreeRegressor()
clf.fit(X, y)
y_pred = clf.predict(X)

print "dt score=", mean_squared_error(y_pred, y)
