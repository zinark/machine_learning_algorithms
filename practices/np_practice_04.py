import numpy as np

# x + 2y = 1
# 3x + 4y = 2
A = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])

solution1, solution2 = np.linalg.inv(A).dot(b), np.linalg.solve(A, b)
print solution1, solution2
