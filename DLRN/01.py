# Forward propagation
import numpy as np

input_data = np.array([3, 5])

weights = {
    'node_0': np.array([2, 4]),
    'node_1': np.array([4, -5]),
    'output': np.array([2, 7])
}


node_0_value = input_data.dot(weights['node_0'])
node_1_value = input_data.dot(weights['node_1'])
hidden_data = np.array([node_0_value, node_1_value])
output_value = hidden_data.dot(weights['output'])

print output_value
