from math import log


def powerof4(n):

    if type(n) in (float, int) and n > 0:
        return log(n, 4).is_integer()
    return False

def powerof4(n):
    if type(n)!=int:
        return False
    return n&(n-1) == 0

if __name__ == '__main__':
    assert powerof4('abc') == False
    assert powerof4(10) == False
    assert powerof4(4) == True
    assert powerof4(True) == False
    assert powerof4(-1) == False
