# linear-equation => y = mx + b
# m : slope
# b : y-intercept

# m = (|x|.|y| - |x.y|) / ( |x|^2 - |y|^2)
# b = |y| - m.|x|

import sympy as sp

x, y, m, b = sp.symbols('x,y,m,b')
m = (abs(x) * abs(y) - abs(x * y)) / (abs(x) ** 2 - abs(y) ** 2)
b = y - m * x

print "(ii) m = "
sp.pprint(m)
print

print "(iii) y = m . x + b --> b ="
sp.pprint(b)
print
