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


def frequency(data, target_attr):
    freq = {}
    for i, row in data.iterrows():
        attr_value = row[target_attr]
        if not freq.has_key(attr_value):
            freq[attr_value] = 0.
        freq[attr_value] += 1.
    return freq


def entropy(data, target_attr):
    freq = frequency(data, target_attr)

    total_entropy = 0.
    for value in freq:
        p = freq[value] / len(data)
        e = -p * math.log(p, 2)
        total_entropy += e
    return total_entropy


def gain(data, attr, target_attr):
    freq = frequency(data, attr)

    subset_entropy = 0.
    for value in freq:
        p = freq[value] / len(data)
        subset = [value] * int(freq[value])
        e = -p * math.log(p, 2)
        print value, freq[value], p, e, subset
        #entropy(subset_entropy)
        subset_entropy += e

    return entropy(data, target_attr)


# print entropy(dt, "a1")
# print entropy(dt, "a2")
# print entropy(dt, "a3")
# print "E(a1)=", entropy(dt, "a1")
# print "E(a2)=", entropy(dt, "a2")
g = gain(dt, "a1", "a2")
# print "GAIN(a1,a2)", g

print entropy(dt, "a")