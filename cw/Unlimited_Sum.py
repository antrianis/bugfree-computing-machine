from __builtin__ import sum as builtin_sum

def sum(*args):
    return builtin_sum(arg for arg in args if isinstance(arg, int))

import unittest
class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sum(10,1), 11)
    def test_2(self):
        self.assertEqual(sum(10), 10)


if __name__ == '__main__':
    unittest.main()