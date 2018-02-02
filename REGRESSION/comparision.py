import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor

df = pd.read_csv("boston.csv")
print df.head()
X = df["lstat"].values.reshape(-1, 1)
y = df["medv"].values

# Cross validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print len(X_train), len(X_test)

# Training
model_lr = LinearRegression()
model_rr = RANSACRegressor()

model_lr.fit(X_train, y_train)
model_rr.fit(X_train, y_train)

pred_train_y = model_lr.predict(X_train)
pred_test_y = model_lr.predict(X_test)
