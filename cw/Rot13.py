from codecs import encode as _dont_use_this_

def rot13(message):
    result = ''
    for m in message:
        if m.isalpha():
            f = ord('a') if m.islower() else ord('A')
            m = chr(((ord(m) - f)  + 13) % 26 + f)
        result+=m
    return result

from string import maketrans, lowercase, uppercase


def rot13_1(message):
    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
    return message.translate(lower).translate(upper)


import unittest


class BobTests(unittest.TestCase):

    def test1(self):
        self.assertEquals(rot13("Test"), "Grfg")

if __name__ == '__main__':
    unittest.main()
