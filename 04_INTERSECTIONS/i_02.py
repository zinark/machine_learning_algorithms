from BSE.Library.CoreLine import CoreLine


def simple_tests():
    global l1, l2
    l1 = CoreLine([1, 1], 1)
    l2 = CoreLine([3, 3], 1)
    print l1, " // ", l2, " -> ", l1.is_parallel(l2)
    print l1, " == ", l2, " -> ", l1.is_equal(l2)
    print "intersection", l1.intersection(l2)
    l1 = CoreLine([-1, 1], 1)
    l2 = CoreLine([1, 1], 2)
    print l1, " // ", l2, " -> ", l1.is_parallel(l2)
    print l1, " == ", l2, " -> ", l1.is_equal(l2)
    print "intersection", l1.intersection(l2)


def test_01():
    global l1, l2
    l1 = CoreLine([4.046, 2.836], 1.21)
    l2 = CoreLine([10.115, 7.09], 3.025)
    print l1, " // ", l2, " -> ", l1.is_parallel(l2)
    print l1, " == ", l2, " -> ", l1 == l2
    print "intersection", l1.intersection(l2)
    l1 = CoreLine([7.204, 3.182], 8.68)
    l2 = CoreLine([8.172, 4.114], 9.883)
    print l1, " // ", l2, " -> ", l1.is_parallel(l2)
    print l1, " == ", l2, " -> ", l1 == l2
    print "intersection", l1.intersection(l2)

test_01()
l1 = CoreLine([1.182, 5.562], 6.744)
l2 = CoreLine([1.773, 8.343], 9.525)
print " // ", l1.is_parallel(l2)
print " == ", l1 == l2
print "intersection", l1.intersection(l2)
