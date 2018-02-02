import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(13, 6))
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor

df = pd.read_csv("boston.csv")
print df.head()
X = df["rm"].values.reshape(-1, 1)
y = df["medv"].values

# Cross validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print len(X_train), len(X_test)


def Diff():
    from sklearn.metrics import r2_score
    # Training on LR
    model_lr = LinearRegression()
    model_lr.fit(X_train, y_train)
    pred_train_y_lr = model_lr.predict(X_train)
    pred_test_y_lr = model_lr.predict(X_test)
    accuracy_lr = model_lr.score(X_test, y_test)
    # Show result of LR
    plt.subplot(211)
    plt.title("Residual analysis for : Linear %f" % r2_score(y_test, pred_test_y_lr))
    plt.scatter(X_train, y_train, color='green', label='training set', marker='+')
    plt.scatter(X_test, y_test, color='red', label='test set', marker='o')
    plt.plot(X_train, pred_train_y_lr, color='yellow', label='prediction on training')
    plt.plot(X_test, pred_test_y_lr, color='blue', label='prediction on test %f' % accuracy_lr)
    plt.legend()
    # Training on RR
    model_rr = RANSACRegressor()
    model_rr.fit(X_train, y_train)
    pred_train_y_rr = model_rr.predict(X_train)
    pred_test_y_rr = model_rr.predict(X_test)
    accuracy_rr = model_rr.score(X_test, y_test)
    # Show result of RR
    plt.subplot(212)
    plt.title("Residual analysis for : Ransac %f" % r2_score(y_test, pred_test_y_rr))
    plt.scatter(X_train, y_train, color='green', label='training set', marker='+')
    plt.scatter(X_test, y_test, color='red', label='test set', marker='o')
    plt.plot(X_train, pred_train_y_rr, color='yellow', label='prediction on training')
    plt.plot(X_test, pred_test_y_rr, color='blue', label='prediction on test %f' % accuracy_rr)
    plt.legend()
    plt.show()


Diff()


def NearlyPerfect():
    global y, X, X_train, X_test, y_train, y_test
    # Bad Model
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_train_pred = lr.predict(X_train)
    y_test_pred = lr.predict(X_test)
    # Nearly Perfect Model
    rnd = np.random.RandomState(0)
    x = 10 * rnd.rand(1000)
    y = x * 3 + rnd.rand(1000)
    X = x.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    lr = LinearRegression()
    lr.fit(X, y)
    y_train_pred = lr.predict(X_train)
    y_test_pred = lr.predict(X_test)
    # Residual Analysis
    plt.scatter(y_train_pred, y_train_pred - y_train, c='blue', marker='o', label='Training data')
    plt.scatter(y_test_pred, y_test_pred - y_test, c='orange', marker='*', label='Test data')
    plt.xlabel("training predictions")
    plt.ylabel("residuals (difference) |prediction - actual|")
    plt.hlines(y=0, xmin=-10, xmax=50, lw=2, color='k')
    plt.xlim([-10, 50])
    plt.ylim([-25, 25])
    plt.grid(linestyle=':')
    plt.legend()
    plt.show()
    # Mean Squared Error (Root Squared Error)
    from sklearn.metrics import mean_squared_error
    print "MSE of train:", mean_squared_error(y_train, y_train_pred)
    print "MSE of test:", mean_squared_error(y_test, y_test_pred)
    # Coefficient of Determination R^2, 1 is perfect
    from sklearn.metrics import r2_score
    print "r2_score of train:", r2_score(y_train, y_train_pred)
    print "r2_score of test:", r2_score(y_test, y_test_pred)
