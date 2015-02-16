import itertools
def last(*args):
    try:
        return args[-1][-1]
    except:
        return args[-1]


assert last(1,2,3) == 3
assert last([1,2,3,4]) == 4
assert last("xyz") == 'z'
assert last(1,2,3,4) == 4
assert last(123) == 123
assert last([1,2,[3,4]]) == 4