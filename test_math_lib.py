import unittest
import math_lib
import random
import statistics as stats
import math


class TestMathLib(unittest.TestCase):

    # Test list_mean
    def test_list_mean_noinput(self):
        A = math_lib.list_mean(None)
        self.assertEqual(A, None)

    def test_list_mean_empty(self):
        A = math_lib.list_mean([])
        self.assertEqual(A, None)

    # Test list_mean constant
    def test_list_mean_constant(self):
        A = math_lib.list_mean([5, 5, 5])
        self.assertEqual(A, 5)

    # Test list_mean random
    def test_list_mean_random_int(self):
        L = []
        for i in range(100):
            L.append(random.randint(0, 100))
        A = math_lib.list_mean(L)
        B = stats.mean(L)
        self.assertEqual(A, B)

    def test_list_mean_random_float(self):
        L = []
        for i in range(100):
            L.append(random.uniform(0, 100))
        A = math_lib.list_mean(L)
        B = stats.mean(L)
        self.assertTrue(math.isclose(A, B))

    # Test list_mean input value not supported
    def test_list_mean_nonint(self):
        L = []
        for i in range(100):
            L.append('A')
        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean(L)
        self.assertEqual(str(ex.exception), 'Unsupported value in list.')

    # Unit test for list_stdev
    def test_list_stdev_noinput(self):
        A = math_lib.list_stdev(None)
        self.assertEqual(A, None)

    def test_list_stdev_empty(self):
        A = math_lib.list_stdev([])
        self.assertEqual(A, None)

    # Test list_stdev constant
    def test_list_stdev_constant(self):
        A = math_lib.list_stdev([5, 5, 5])
        self.assertEqual(A, 0)

    # Test list_stdev random
    def test_list_stdev_random_int(self):
        L = []
        for i in range(100):
            L.append(random.randint(0, 100))
        A = math_lib.list_stdev(L)
        B = stats.stdev(L)
        self.assertTrue(math.isclose(A, B))

    def test_list_stdev_random_float(self):
        L = []
        for i in range(100):
            L.append(random.uniform(0, 100))
        A = math_lib.list_stdev(L)
        B = stats.stdev(L)
        self.assertTrue(math.isclose(A, B))

    # Test list_mean input value not supported
    def test_list_stdev_nonint(self):
        L = []
        for i in range(100):
            L.append('A')
        with self.assertRaises(ValueError) as ex:
            math_lib.list_stdev(L)
        self.assertEqual(str(ex.exception), 'Unsupported value in list.')


if __name__ == '__main__':
    unittest.main()
