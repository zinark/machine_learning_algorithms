from Library.CoreVector import *
import matplotlib.pyplot as plt


def q01():
    v1 = CoreVector([8.218, -9.341])
    v2 = CoreVector([-1.129, 2.111])
    print v1, "+", v2, "=", v1.plus(v2)
    v1 = CoreVector([7.119, 8.215])
    v2 = CoreVector([-8.223, 0.878])
    print v1, "+", v2, "=", v1.sub(v2)
    s = 7.41
    v1 = CoreVector([1.671, -1.012, -0.318])
    print s, "*", v1, "=", v1.scale(s)
    v1 = CoreVector([-0.221, 7.437])
    v2 = CoreVector([8.813, -1.331, -6.247])
    print "Magnitudes"
    print round(v1.magnitude(), 3), round(v2.magnitude(), 3)
    v1 = CoreVector([5.581, -2.136])
    v2 = CoreVector([1.996, 3.108, -4.554])
    print "Directions"
    print v1.normalized(), v2.normalized()
    # v.w = ||v||.||w||.cos(t)


def q_dots_and_angles():
    print "DotProduct = ", round(CoreVector([7.887, 4.138])
                                 .dot(CoreVector([-8.802, 6.776])), 3)
    print "DotProduct = ", round(CoreVector([-5.955, -4.904, -1.874])
                                 .dot(CoreVector([-4.496, -8.755, 7.103])), 3)
    print "Angle in Radiant = ", CoreVector([3.183, -7.627]).angle_with(CoreVector([-2.668, 5.319]))
    print "Angle in Degree = ", CoreVector([7.35, 0.221, 5.188]).angle_with(CoreVector([2.751, 8.259, 3.985]),
                                                                            in_degrees=True)


def q_parallel_vs_orthogonal():
    v = CoreVector([-7.579, -7.88])
    w = CoreVector([22.737, 23.64])
    print "P | O --> T F, actual = ", v.is_parallel_with(w), v.is_orthogonal_with(w)
    v = CoreVector([-2.029, 9.97, 4.172])
    w = CoreVector([-9.231, -6.639, -7.245])
    print "P | O --> F F, actual = ", v.is_parallel_with(w), v.is_orthogonal_with(w)
    v = CoreVector([-2.328, -7.284, -1.214])
    w = CoreVector([-1.821, 1.072, -2.94])
    print "P | O --> F T, actual = ", v.is_parallel_with(w), v.is_orthogonal_with(w)
    v = CoreVector([2.118, 4.827])
    w = CoreVector([0, 0])
    print "P | O --> T T, actual", v.is_parallel_with(w), v.is_orthogonal_with(w)


def q_projections():
    v = CoreVector([3.039, 1.879])
    b = CoreVector([0.825, 2.036])
    print "Projection=", v.component_parallel_to(b)
    v = CoreVector([-9.88, -3.264, -8.159])
    b = CoreVector([-2.155, -9.353, -9.473])
    print "Projection Component=", v.component_orthogonal_to(b)
    v = CoreVector([3.009, -6.172, 3.692, -2.51])
    b = CoreVector([6.404, -9.144, 2.759, 8.718])
    print "Projection and its Component=", v.component_parallel_to(b), v.component_orthogonal_to(b)


def q_cross_products():
    v = CoreVector([8.462, 7.893, -8.187])
    w = CoreVector([6.984, -5.975, 4.778])
    print "1", v.cross_product(w)
    v = CoreVector([-8.987, -9.838, 5.031])
    w = CoreVector([-4.268, -1.861, -8.866])
    print "2", v.area_of_parallelogram(w)
    v = CoreVector([1.5, 9.547, 3.691])
    w = CoreVector([-6.007, 0.124, 5.772])
    print "3", v.cross_product(w), v.area_of_parallelogram(w) / 2
