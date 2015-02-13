import math


def check_length(func):
    def wrapper(a, b):
        if not (len(a.values) == len(b.values)):
            raise ValueError()
        return func(a, b)
    return wrapper


class Vector:
    def __init__(self, values):
        self.values = values

    @check_length
    def add(self, other):
        return Vector([a + b for a, b in zip(self.values, other.values)])

    @check_length
    def subtract(self, other):
        return Vector([a - b for a, b in zip(self.values, other.values)])

    @check_length
    def dot(self, other):
        return sum(a * b for a, b in zip(self.values, other.values))

    def norm(self):
        return math.sqrt(sum(a ** 2 for a in self.values))

    def __str__(self):
        return '(' + ','.join(str(a) for a in self.values) + ')'

    def equals(self, other):
        return all(a == b for a, b in zip(self.values, other.values))
