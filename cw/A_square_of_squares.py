from math import sqrt


def is_square(n):
    try:
        return int(sqrt(n)) == sqrt(n)
    except Exception:
        return False


def is_square2(n):
    return n > 0 and sqrt(n).is_integer()
