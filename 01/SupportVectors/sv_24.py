import numpy as np

import Library.CoreML

data_dict = {
    -1: np.array([[1, 7], [2, 8], [3, 8]]),
    +1: np.array([[5, 1], [6, -1], [7, 3]])
}

svm = Library.CoreML.CoreSVM()
svm.fit(data_dict)
svm.visualize()
result = svm.predict([1, 3])
print result
