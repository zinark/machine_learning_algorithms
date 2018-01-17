import numpy as np

import Library.CoreML

data_dict = {
    -1: np.array([[1, 7], [2, 8], [3, 8]]),
    +1: np.array([[5, 1], [6, -1], [7, 3]])
}

svm = Library.CoreML.CoreSVM()
svm.fit(data_dict)
pts = [[0, 10], [1, 3], [3, 4], [3, 5], [5, 5], [5, 6], [6, -6], [5, 8]]
for pt in pts:
    result = svm.predict(pt)
    print result
svm.visualize()
