import numpy as np

i = np.array([1,1])
w0 = np.array([2,4])
w1 = np.array([4,-5])

x0 = w0.dot(i)
x1 = w1.dot(i)
layer1 = np.array([x0, x1])

w2 = np.array([0, 1])
w3 = np.array([1, 1])

x2 = w2.dot(layer1)
x3 = w3.dot(layer1)

layer2 = np.array([x2, x3])

woutput = np.array([5,1])
output = woutput.dot(layer2)

print output