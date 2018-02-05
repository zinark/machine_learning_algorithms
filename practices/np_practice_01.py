import numpy as np

A = np.array([1, 2, 3])
A ** 2
np.sqrt(A ** 2)
np.exp(A), np.log(A)

# a.b = a_t . b = sum(i in N) (ai * bi)
# a.b = |a||b|cosO(a,b)
# angle(a,b) = a_t * b / |a||b|

a = np.array([1, 2])
b = np.array([2, 1])
dot_product_0 = 0
for i, j in zip(a, b):
    dot_product_0 += a * b

dot_product_1 = np.sum(a * b)
dot_product_2 = (a * b).sum()
dot_product_3 = a.dot(b)

angle = np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))
print "angle", np.arccos(angle)