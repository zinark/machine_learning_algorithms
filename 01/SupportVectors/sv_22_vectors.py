import unittest
import numpy as np
from Library.CoreML import CoreML
import sympy as sp
from sympy.physics.vector import ReferenceFrame
import matplotlib.pyplot as plt


class Vectors(unittest.TestCase):

    def equation_for_sv(self):
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
        sp.pprint(sp.solve([eq2, eq1]))

        # optimization f = minimize 1/||w||^2
        # constraints = yi (x . w + b) - 1

    def test_parts_of_svm(self):
        u = np.array([2.5, 2.5])
        w = np.array([2, 2])

        pseries = np.array([[4, 4], [5, 5], [3, 5]])
        nseries = np.array([[0, 1], [1, 0], [2, 1]])

        plt.scatter(nseries[0:, 0], nseries[0:, 1], c='r')
        plt.scatter(pseries[0:, 0], pseries[0:, 1], c='g')
        plt.plot([0, w[0]], [0, w[1]])
        plt.scatter([u[0]], [u[1]], s=150, c='b')

        # (a.i)       w . u >= c                w-projection on u
        # (a.ii)      w . u + b >= 0            decision-rule-f
        # (a.iii)     b = -c

        f_decision_rule = [w.dot(u) + b for b in np.arange(0, 5, 0.1)]
        plt.plot(np.arange(0, 5, 0.1), f_decision_rule, c='y')

        # Positive and negative Samples
        # (b.i)         w . xp + b >= 1
        # (b.ii)        w . xn + b <= -1

        for x in pseries:
            pos_vals = [w.dot(x) + b for b in np.arange(0, 5, 0.1)]
            plt.plot(np.arange(0, 5, 0.1), pos_vals, c='g')

        for x in nseries:
            pos_vals = [w.dot(x) + b for b in np.arange(0, 5, 0.1)]
            plt.plot(np.arange(0, 5, 0.1), pos_vals, c='r')

        plt.show()
