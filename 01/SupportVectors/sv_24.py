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
