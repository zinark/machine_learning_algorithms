import numpy as np
import matplotlib.pyplot as plt


def fit(X, y):
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    return np.linalg.solve(X.transpose().dot(X), X.transpose().dot(y))


def make_poly(X, degree):
    assert isinstance(X, np.ndarray)
    return np.vstack([X ** i for i in range(degree)]).transpose()


def mse(y, ypred):
    assert isinstance(y, np.ndarray)
    assert isinstance(ypred, np.ndarray)
    delta = y - ypred
    return delta.dot(delta) / len(y)


np.random.seed(1)
random_force = 0.2
f = lambda l: random_force * np.random.rand() + l ** 0 + \
              random_force * np.random.rand() + l ** 1 + \
              random_force * np.random.rand() + l ** 49 + \
              random_force * np.random.rand() + l ** 101

# inputs
x_train = np.random.random(500)
y_train = np.array([f(v) for v in x_train])
x_test = np.random.random(100)
y_test = np.array([f(v) for v in x_test])

plt.figure(figsize=(18, 12))
fno = 440
plt.subplots_adjust(hspace=0.6)
for polynomial_degree in range(3, 12):
    fno = fno + 1
    plt.subplot(fno)
    plt.scatter(x_train, y_train, s=.1, c='green', label='training data')
    plt.scatter(x_test, y_test, s=.1, c='red', label='test data')
    inputs_train = make_poly(x_train, polynomial_degree)
    inputs_test = make_poly(x_test, polynomial_degree)
    ypred_train = inputs_train.dot(fit(inputs_train, y_train))
    ypred_test = inputs_test.dot(fit(inputs_test, y_test))
    mse_train = round(mse(y_train, ypred_train), 3)
    mse_test = round(mse(y_test, ypred_test), 3)
    plt.title("Training Error: {0:.5f}\nTest Error: {0:.5f}".format(mse_train, mse_test))
    #plt.suptitle("Test Error: {0:.5f}".format(mse_test))
    lbl = "degree:{0:d}".format(polynomial_degree)
    plt.plot(sorted(x_train), sorted(ypred_train), label=lbl, color='k')
    plt.grid(ls=':')
    plt.legend()

plt.show()
