# hyperplane = x . w + b = 0
# x . w + b =  1     for pos Support vector
# x . w + b = -1     for neg "

# opt-obj = min ||w||
#           max b

# constrains : yi (xi . w + b) >= 1
# it's boiled down to : Class (Features . w + b) >= 1,        maximize b and minimize w

# solving convex opt problems:
# libsvm : https://www.csie.ntu.edu.tw/~cjlin/libsvm/
# cvxopt : http://cvxopt.org/examples/index.html

import numpy as np

import Library.CoreML

data_dict = {
    -1: np.array([[1, 7], [2, 8], [3, 8]]),
    +1: np.array([[5, 1], [6, -1], [7, 3]])
}

svm = Library.CoreML.CoreSVM()
svm.fit(data_dict)
result = svm.predict([1, 3])
print result
