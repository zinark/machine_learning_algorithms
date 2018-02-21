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

weights_updated = weights - (learning_rate * slope)
print weights, weights_updated

preds_updated = weights_updated.dot(input_data)
print preds, preds_updated

error_updated = preds_updated - target
print error, error_updated