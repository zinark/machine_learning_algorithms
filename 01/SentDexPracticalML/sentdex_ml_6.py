import pickle
import numpy as np
import math

import sklearn.linear_model
from sklearn import *
import quandl as Quandl


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

    forecast_col = 'Adj. Close'
    forecast_out_quantity = int(math.ceil(0.01 * len(data)))  # Onda birindeki satir
    data['label'] = data[forecast_col].shift(-forecast_out_quantity)
    data.dropna(inplace=True)

    x_dropped = np.array(data.drop(['label'], 1))
    y = np.array(data['label'])

    x_scaled = preprocessing \
        .scale(x_dropped)  # x_scaled_min_max = sklearn.preprocessing.MinMaxScaler().fit_transform(x_train)

    x = x_scaled
    print len(x), len(y)
    return x, y, data, forecast_out_quantity


X, Y, df, forecast_len = import_data()
x_train, x_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.3)

# classifier = sklearn.linear_model.LinearRegression()
# classifier.fit(x_train, y_train)
#
# # Dump fitting process by using pickle
# with open('fit.pickle', 'wb') as f:
#     pickle.dump(classifier, f)
#     pass

fit_input = open('fit.pickle', 'rb')
classifier = pickle.load(fit_input)

print "accuracy", classifier.score(x_test, y_test)