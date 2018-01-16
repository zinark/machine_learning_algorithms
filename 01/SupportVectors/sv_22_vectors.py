import unittest
import numpy as np
from Library.CoreML import CoreML
import sympy as sp
from sympy.physics.vector import ReferenceFrame


class Vectors(unittest.TestCase):

    def test_equation_for_sv(self):
        w1, w2, x1, x2, y1, y2 = sp.symbols("w1, w2, x1, x2, y1, y2")

        R = ReferenceFrame("R")
        x_pos = x1 * R.x + y1 * R.y
        x_neg = x2 * R.x + y2 * R.y
        w = w1 * R.x + w2 * R.y

        x3, y3, b = sp.symbols("x3, y3, b")
        x = x3 * R.x + y3 * R.y
        eq1 = (x_pos - x_neg).dot(w / w.magnitude())
        eq2 = (x.dot(w) + b) - 1
        sp.pprint(eq1)
        sp.pprint(eq2)

        sp.pprint(sp.solve(eq1))
        sp.pprint(sp.solve(eq2))
        sp.pprint(sp.solve([eq2,eq1]))
