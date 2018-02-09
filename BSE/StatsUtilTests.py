import sys

sys.path.append("..")
from unittest import TestCase

from BSE.StatsUtil import StatsUtil


class StatsUtilTests(TestCase):

    def test_mean(self):
        f = lambda x: StatsUtil.mean(x)
        self.assertEqual(1, f([1, 1, 1]))
        self.assertEqual(2, f([1, 2, 3]))
        self.assertEqual(111. / 3, f([1, 10, 100]))

    def test_median(self):
        f = lambda x: StatsUtil.median(x)
        self.assertEqual(1, f([1, 1, 1]))
        self.assertEqual(2, f([1, 2, 3]))
        self.assertEqual(10, f([1, 10, 100]))
        self.assertEqual(7. / 2, f([1, 2, 5, 10, -20, 20]))
        self.assertEqual(5, f([1, 2, 5, 10, 20]))

    def test_mode(self):
        f = lambda x: StatsUtil.mode(x)
        self.assertEqual(5, f([1, 5, 5, 2, 5, 10, -20, 20]))
        self.assertEqual(1, f([1, 1, 1, 2]))
        self.assertEqual(3, f([1, 2, 3]))
        i =[88.629999999999995, 37.640000000000001, 60.340000000000003, 9.5999999999999996, 46.700000000000003,
             9.5999999999999996, 35.07, 20.469999999999999, 29.059999999999999, 12.369999999999999, 9.5999999999999996,
             8.3399999999999999, 30.280000000000001, 91.659999999999997, 55.700000000000003, 10.93, 87.219999999999999,
             92.5, 4.3700000000000001, 81.420000000000002, 10.65, 51.539999999999999, 34.460000000000001,
             87.420000000000002, 90.010000000000005, 80.530000000000001, 99.010000000000005, 39.009999999999998,
             5.7300000000000004, 94.780000000000001, 36.359999999999999, 18.079999999999998, 87.959999999999994]
        self.assertEqual(9.6, f(i))


    def test_variance(self):
        f = lambda x: StatsUtil.variance(x)
        self.assertEqual(62.572884, f([13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]))

    def test_standard_deviation(self):
        f = lambda x: StatsUtil.std_deviation(x)
        self.assertEqual(7.9103023962425105, f([13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]))