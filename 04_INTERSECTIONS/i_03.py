from BSE.Library.CorePlane import CorePlane
from BSE.Library.CoreVector import CoreVector


def t01():
    p1 = CorePlane([-0.412, 3.806, 0.728], -3.46)
    p2 = CorePlane([1.03, -9.515, -1.82], 8.65)
    print "//", p1.is_parallel(p2)
    print "==", p1 == p2
    p1 = CorePlane([2.611, 5.528, 0.283], 4.6)
    p2 = CorePlane([7.715, 8.306, 5.342], 3.76)
    print "//", p1.is_parallel(p2)
    print "==", p1 == p2
    p1 = CorePlane([-7.926, 8.625, -7.212], -7.952)
    p2 = CorePlane([-2.642, 2.875, -2.404], -2.443)
    print "//", p1.is_parallel(p2)
    print "==", p1 == p2


