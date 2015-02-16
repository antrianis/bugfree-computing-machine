
def toJadenCase(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split())

def toJadenCase2(string):        
    return " ".join(w.capitalize() for w in string.split())

import string
def toJadenCase3(string1):
    return string.capwords(string1)


import unittest
class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(toJadenCase('hello maria'), 'Hello Maria')
    def test_2(self):
        self.assertEqual(toJadenCase('HI J'), 'HI J')
    def test_3(self):
        self.assertEqual(toJadenCase(''), '')


if __name__ == '__main__':
    unittest.main()