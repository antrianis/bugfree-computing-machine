t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    sn = str(n)

    try:
        max_value = max([x for x in sn if x != '0'])
        max_index = sn.index(max_value)
    except ValueError:
        max_index = -1

    try:
        min_value = min([x for x in sn if x != '0'])
        min_index = sn.index(min_value)
    except ValueError:
        min_index = -1

    min_num = max_num = sn
    if len(sn) > 1 and min_index != -1:
        if sn[0] != max_value:
            max_num = max_value + sn[1:max_index] + sn[0] + sn[max_index+1:]
        if sn[0] != min_value:
            min_num = min_value + sn[1:min_index] + sn[0] + sn[min_index+1:]

    print 'Case #{}: {} {}'.format(i+1, min_num, max_num)

















