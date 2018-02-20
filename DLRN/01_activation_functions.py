import numpy as np


def relu(x):
    return max(x, 0)
    # if x < 0:
    #     return 0
    # if x >= 0:
    #     return x


def predict_with_network(input_data_row, weights):
    node_0_input = input_data_row.dot(weights['node_0'])
    node_0_output = relu(node_0_input)

    node_1_input = input_data_row.dot(weights['node_1'])
    node_1_output = relu(node_1_input)

    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    output = hidden_layer_outputs.dot(weights['output'])
    # output = relu(hidden_layer_outputs)
    return output


input_data = [
    np.array([3, 5]),
    np.array([1, -1]),
    np.array([0, 0]),
    np.array([8, 4])
]
weights = {
    'node_0': np.array([2, 4]),
    'node_1': np.array([4, -5]),
    'output': np.array([2, 7])
}

results = []
for i in input_data:
    results.append (predict_with_network(i, weights))

print results