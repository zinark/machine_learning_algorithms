import math
import pandas as pd

inputs = {
    "a1": [0, 0, 1, 1, 1],
    "a2": [1, 1, 0, 1, 1],
    "a3": [0, 0, 0, 0, 1],
    "outs": ["Yes", "Yes", "No", "No", "Yes"]
}

dt = pd.DataFrame(inputs)

print dt


def entropy(data, target_attr):
    freq = {}
    for i, row in data.iterrows():
        attr_value = row[target_attr]
        if not freq.has_key(attr_value):
            freq[attr_value] = 0.
        freq[attr_value] += 1.

    total_entropy = 0.
    for i in freq:
        p = freq[i] / len(data)
        e = -p * math.log(p, 2)
        # print i, freq[i], p, e
        total_entropy += e
    return total_entropy

print entropy(dt, "a1")
print entropy(dt, "a2")
print entropy(dt, "a3")
