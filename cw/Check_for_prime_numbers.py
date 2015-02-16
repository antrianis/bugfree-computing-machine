import unittest
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(sqrt(n) + 1),2):
        if n % i == 0:
            return False
    return True


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(4), False)        


if __name__ == '__main__':
    unittest.main()