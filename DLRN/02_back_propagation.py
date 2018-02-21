from sklearn.metrics import mean_squared_error
import numpy as np


def draft_01():
    l1 = np.array([
        np.array([3, 2]).dot([2, 1]),
        np.array([3, 2]).dot([0, 0])
    ])
    output = l1.dot([2.01, 2])
    print output - 7


weights_0 = {
    'node_0': np.array([2, 1]),
    'node_1': np.array([1, 2]),
    'output': np.array([1, 1])
}

weights_1 = {
    'node_0': np.array([2, 1]),
    'node_1': np.array([1., 1.5]),
    'output': np.array([1., 1.5])
}

input_data = [
    np.array([0, 3]),
    np.array([1, 2]),
    np.array([-1, -2]),
    np.array([4, 0])
]

target_actuals = [1, 3, 5, 7]


def relu(x):
    return max(x, 0)


def predict_with_network(input_data_row, weights):
    node_0_input = input_data_row.dot(weights['node_0'])
    node_0_output = relu(node_0_input)

    node_1_input = input_data_row.dot(weights['node_1'])
    node_1_output = relu(node_1_input)

    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    output = hidden_layer_outputs.dot(weights['output'])
    return output

#
# model_output_0 = []
# model_output_1 = []
#
# for row in input_data:
#     model_output_0.append(predict_with_network(row, weights=weights_0))
#     model_output_1.append(predict_with_network(row, weights=weights_1))
#
# # Calculate the mean squared error for model_output_0: mse_0
# mse_0 = mean_squared_error(target_actuals, model_output_0)
# mse_1 = mean_squared_error(target_actuals, model_output_1)
#
# # Print mse_0 and mse_1
# print("Mean squared error with weights_0: %f" % mse_0)
# print("Mean squared error with weights_1: %f" % mse_1)

from sklearn.metrics import mean_squared_error

model_output_0 = []
model_output_1 = []

for row in input_data:
    print (row)
    model_output_0.append(predict_with_network(row, weights_0))
    model_output_1.append(predict_with_network(row, weights_1))

mse_0 = mean_squared_error(target_actuals, model_output_0)
mse_1 = mean_squared_error(target_actuals, model_output_1)

print("Mean squared error with weights_0: %f" %mse_0)
print("Mean squared error with weights_1: %f" %mse_1)
