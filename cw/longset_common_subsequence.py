def lcs(x, y, res=''):
    if not x or not y:
        return res
    res1,res2,res3 = "", "", ""
    if x[0] == y[0]:
        res1 = lcs(x[1:], y[1:], res + str(x[0]))
    else:       
        res2 = lcs(x, y[1:], res)
        res3 = lcs(x[1:], y, res)
    max1 = res1 if len(res1) > len(res2) else res2
    max2 = res3 if len(res3) > len(max1) else max1
    return max2

