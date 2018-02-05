import numpy as np
import random

L = [[1, 2], [3, 4]]
M1 = np.array(L)
M2 = np.matrix(L)
M3 = M1.T
np.array([1, 2, 3])
ZEROS1 = np.zeros(4)
ZEROS2 = np.zeros((4, 3))
ONES = np.ones(4)
R1 = np.random.random((3, 2))
R2 = 10 * np.random.random((3, 2))
G = np.random.randn(10, 10)
m1, v1 = ONES.mean(), ONES.var()
m2, v2 = G.mean(), G.var()

a = 1
r1 = random.Random().randint(1, 50)
r2 = random.Random().randint(1, 50)
DOT = np.dot(np.ones((r1, a)), np.ones((a, r1)))

M10 = np.array([[1,2], [3,4]])
INV = np.linalg.inv(M10)
IDENTITY = INV.dot(M10)
DET = np.linalg.det(M10)
DIAG = np.diag(M10)

a=np.array([1,2])
b=np.array([3,4])
print np.outer(a,b)
print np.inner(a,b), np.dot(a,b)
print np.diag(M10).sum(), np.trace(M10)

mat1 = np.random.randn(5, 3)
print mat1
# print np.linalg.eig(mat1)
np.cov(mat1), np.cov(mat1).shape
np.cov(mat1.T), np.cov(mat1.T).shape
np.linalg.eigh(np.cov(mat1.T))
np.linalg.eig(np.cov(mat1.T))

