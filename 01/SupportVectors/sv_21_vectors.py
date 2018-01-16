import unittest
import numpy as np

from Library.CoreML import CoreML


class Vectors(unittest.TestCase):
    def test_magnitude_of_an_vector(self):
        vector = [3, 4]
        origin = [0, 0]
        self.assertEqual(5, np.linalg.norm(np.array(vector)))
        self.assertEqual(5, CoreML.euclidean_distance(vector))
        self.assertEqual(5, CoreML.euclidean_distance(vector, origin))

    def test_dot_products(self):
        a = [1, 3, 5]
        b = [4, 2, 5]
        dotproduct = 35
        self.assertEqual(dotproduct, np.dot(a, b))
        self.assertEqual(dotproduct, CoreML.dot_products(a, b))