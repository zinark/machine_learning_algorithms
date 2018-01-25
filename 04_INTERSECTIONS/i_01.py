# Ax + By = 0
# [A,B] . [x,y] = 0
from BSE.Library.CoreVector import CoreVector


def parameterizetion_of_line():
    base_point = CoreVector([10, 0])
    direction = CoreVector([1, 5])
    vlist = []
    for t in range(-3, 3, 1):
        vlist.append(base_point.plus(direction.scale(t)))
    for i in vlist:
        print i


def core_equation(m, b, x):
    m = CoreVector([1, m])
    b = CoreVector([0, b])
    # y = m * x + b
    return m.scale(x).plus(b).coords[1]


def parameterization_of_line_2():
    for t in range(-3, 3, 1):
        print core_equation(2, 10, t)


