import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.models import Sequential, load_model, save_model
from keras.utils import to_categorical

df = pd.read_json('titanic.json')
assert isinstance(df, pd.DataFrame)

# corr = df.corr()
# corr[corr <.3] = 0
# plt.imshow (corr, cmap='Blues')
# cols = corr.columns
# n_cols = len(cols)
# plt.xticks(range(n_cols), cols, rotation=90)
# plt.yticks(range(n_cols), cols)
# plt.show()

X = df.drop('survived', axis=1).values
n_features = X.shape[1]

y = df['survived'].values
y_cats = to_categorical(y)

model = Sequential()
model.add(Dense (32, activation='relu', input_shape=(n_features, )))
model.add(Dense (2, activation='softmax'))

model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X, y_cats, epochs=10)
model.save('m.h5')
m2 = load_model('m.h5')
predictions = m2.predict(X[0:1])
#print predictions[:, ,1]

