from math import sqrt


def euclidean_distance(pt1, pt2):
    dimension = len(pt1)
    total = 0
    for i in range(dimension):
        total += (pt1[i] - pt2[i]) ** 2
    return sqrt(total)


# 2 boyutlu
pt1 = [1, 3]
pt2 = [2, 5]
print "2d ed=", euclidean_distance(pt1, pt2), sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# 3 boyutlu
pt1 = [1, 3, 2]
pt2 = [2, 5, 3]
print "3d ed=", euclidean_distance(pt1, pt2), sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 + (pt1[2] - pt2[2]) ** 2)

# 4 boyutlu
pt1 = [1, 3, 2, 9]
pt2 = [2, 5, 3, 10]
print "4d ed=", euclidean_distance(pt1, pt2), sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 + (pt1[2] - pt2[2]) ** 2 + (pt1[3] - pt2[3]) ** 2)

# 5 boyutlu
pt1 = [1, 3, 2, 9, 1]
pt2 = [2, 5, 3, 10, 8]
print "4d ed=", euclidean_distance(pt1, pt2), sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 + (pt1[2] - pt2[2]) ** 2 + (pt1[3] - pt2[3]) ** 2 + + (pt1[4] - pt2[4]) ** 2)
