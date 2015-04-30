def sum_pairs(ints, s):
    #remove consequitive dups
    nints = [ints[i-1] for i in range(1, len(ints)) if not ints[i] == ints[i-1]]
    nints.append(ints[i])

    res,minj = None, len(nints)
    for i in range(len(nints)):
        for j in range(i+1, minj):
            if nints[i] + nints[j] == s:
                res = [nints[i], nints[j]]
                minj = j + 1
    return res
