def midpoint_sum(ints):
    for i in range(1, len(ints)-1):
        if sum(ints[:i]) == sum(ints[i+1:]):
            return i
    return None


assert midpoint_sum([0, 1, 3, 1, 0]) == 2
