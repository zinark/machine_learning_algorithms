import numpy as np

# 2 * x * (y-xb)
input_data = np.array([1, 2, 3])
weights = np.array([0, 2, 1])
target = 0

preds = weights.dot(input_data)
error = preds - target

slope = input_data * error * 2

print slope

learning_rate = 0.01

n_updates = 20
mse_hist = []


def get_mse(input_data_, target_, weights_):
    return input_data_.dot(weights_) - target


def get_slope(input_data_, target_, weights_):
    return input_data_ * get_mse(input_data_, target_, weights_) * 2


# Iterate over the number of updates
for i in range(n_updates):
    # Calculate the slope: slope
    slope = get_slope(input_data, target, weights)

    # Update the weights: weights
    print 'input_data        ', input_data
    print 'mean_squared_error', get_mse(input_data, target, weights)
    print 'slope             ', get_slope(input_data, target, weights)

    print i,'.step -> ',weights, '-', 0.01, '*', slope
    weights = weights - 0.01 * slope
    print '\tweights :', weights

    # Calculate mse with new weights: mse
    mse = get_mse(input_data, target, weights)

    # Append the mse to mse_hist
    mse_hist.append(mse)

# Plot the mse history
# plt.plot(mse_hist)
# plt.xlabel('Iterations')
# plt.ylabel('Mean Squared Error')
# plt.show()
