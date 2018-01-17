import numpy as np
import sympy as sp

# http://mathworld.wolfram.com/MethodofSteepestDescent.html
x1, x2 = sp.symbols("x1, x2")
f = x1 ** 2 + x2 ** 2 - 2 * x1 * x2

gx1 = sp.diff(f, x1)
gx2 = sp.diff(f, x2)
gradf = [gx1, gx2]

lx1 = sp.lambdify((x1, x2), gx1, "numpy")
lx2 = sp.lambdify((x1, x2), gx2, "numpy")
fx = sp.lambdify((x1, x2), f, "numpy")
# print "f and its gradient "
# sp.pprint(f)
# sp.pprint(gradf)
t = 0

done = False

# 1. Start from a random point
x = np.array([3, 1])

while not done:
    # 2. Find the gradient and norm
    r1 = lx1(x[0], x[1])
    r2 = lx2(x[0], x[1])
    gval = np.array([r1, r2], dtype=np.float16)
    norm_of_gval = np.linalg.norm(gval)

    if norm_of_gval <= 0:
        print "---------------------> x:", x, "total-step:", t
        done = True

    # 3. direction is -gval
    direction = -1 * gval

    # 4. calculate the step size

    # a = sp.symbols("a")
    # sp.pprint(f)
    # sp.pprint(f.replace(x1, a))
    # sp.pprint(f.replace(x1, a).replace(x2, a))
    step = 0.15

    print x, direction, direction * step + x
    # a = diff[0] - diff[1]


    # 5. decide what is the next point
    x = x + step * direction
    t += 1
