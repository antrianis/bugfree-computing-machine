def sum_rec(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_rec(lst[1:])

print sum_rec([1,2,3])
print sum_rec([1])
