import numpy as np

f1 = np.sort(np.array([17, 19, 18, 17, 19]))
f2 = np.sort(np.array([7, 38, 4, 23, 18]))

print f1
print f1.mean(), np.median(f1)
print f1.var(), f1.std()

print f2
print f2.mean(), np.median(f2)
print f2.var(), f2.std()

f3 = np.sort(np.array([15, 20, 25, 30, 35]))
print f3.var()

f4 = np.array([3, 3, 3, 3, 3])
print f4.mean(), f4.var(), f4.std()