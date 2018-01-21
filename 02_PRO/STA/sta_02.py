import matplotlib.pyplot as plt
# histogram

data_x = [
    132.754,
    137.192,
    122.177,
    147.121,
    143.000,
    126.010,
    129.200,
    124.312,
    128.132
]
hist_x = [
    lambda x: x < 120,
    lambda x: 120 <= x <= 130,
    lambda x: 130 <= x <= 140,
    lambda x: 140 < x,
]

data_x = [21,17,9,27,12,35,4,32,12,14,38,9,21,19,22,14,3,8,15,31,33,29]
hist_x = [
    lambda x: 0 <= x < 10,
    lambda x: 10 <= x < 20,
    lambda x: 20 <= x < 30,
    lambda x: 30 <= x < 40,
]

freq = {}
for i in data_x:
    for l in hist_x:
        freq_index = hist_x.index(l)
        if not freq.has_key(freq_index):
            freq[freq_index] = 0
        if l(i):
            freq[freq_index] += 1

print freq

plt.bar(freq.keys(), freq.values())
plt.show()