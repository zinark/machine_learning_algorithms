import datetime
import quandl as Quandl, math, pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style


def import_data():
    data = Quandl.get('WIKI/GOOGL')
    data = data[[
        'Adj. Open',
        'Adj. High',
        'Adj. Low',
        'Adj. Close',
        'Adj. Volume']]

    data['HL_PCT'] = (data['Adj. High'] - data['Adj. Close']) / data['Adj. Close'] * 100
    data['PCT_change'] = (data['Adj. Close'] - data['Adj. Open']) / data['Adj. Open'] * 100
    data = data[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
    data.fillna(-99999, inplace=True)
    return data


def decide_features_and_labels(data):
    forecast_col = 'Adj. Close'
    forecast_out_quantity = int(math.ceil(0.01 * len(data)))  # Onda birindeki satir
    data['label'] = data[forecast_col].shift(-forecast_out_quantity)
    data.dropna(inplace=True)
    return data, forecast_out_quantity


def pre_process_data(data):
    x_train = np.array(data.drop(['label'], 1))
    y = np.array(data['label'])
    x_scaled = preprocessing.scale(x_train)
    x_scaled_min_max = preprocessing.MinMaxScaler().fit_transform(x_train)
    x = x_scaled
    print len(x), len(y)
    return x, y


df = import_data()
df, forecast_out = decide_features_and_labels(df)
X, Y = pre_process_data(df)
X_lately = X[-forecast_out:]


def split_data():
    return cross_validation.train_test_split(X, Y, test_size=0.2)


X_train, X_test, Y_train, Y_test = split_data()


def accuracy_for_linear_regression():
    # Simple linear regression
    classifier = LinearRegression(n_jobs=-1)
    classifier.fit(X_train, Y_train)  # Train
    return classifier.score(X_test, Y_test)  # Test


# Support vector regression
classifier = svm.SVR()
classifier.fit(X_train, Y_train)  # Train
accuracy = classifier.score(X_test, Y_test)  # Test

forecast_set = classifier.predict(X_lately)
print forecast_set, accuracy, forecast_out

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 24 * 60 * 60
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
