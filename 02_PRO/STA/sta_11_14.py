def fb(p0, p1, p2):
    j1 = p0 * p1
    j2 = (1 - p0) * (1 - p2)
    return j1 / (j2 + j1)


print fb(.1, .9, .8)
print fb(.01, .7, .9)

def fb_n(p0, p1, p2):
    j1 = p0 * (1-p1)
    j2 = (1 - p0) * (p2)
    return j1 / (j2 + j1)


print fb_n(.1, .9, .8)
print fb_n(.01, .7, .9)


def f(p):
    return 3. * p * (1 - p) * (1 - p)
    # TTT
    # TTH -
    # THT -
    # THH

    # HTT -
    # HTH
    # HHT
    # HHH


# print f(.5)  # .375
# print f(.8)  # .096

p_c1 = p0 = 0.3
p_c2 = 1 - p_c1
p_h_c1 = p1 = .5
p_h_c2 = p2 = .9

p_h = p_c1 * p_h_c1 + p_c2 * p_h_c2
# print p_h
