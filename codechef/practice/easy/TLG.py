if __name__ == '__main__':

    r = int(raw_input())
    l = 0
    w = 0
    p1, p2 = 0 , 0

    for i in range(r):
        cp1, cp2 = map(int, raw_input().split())
        p1 += cp1
        p2 += cp2

        if p1 > p2:
            cl = p1 - p2
            cp = 1
        elif p2 > p1:
            cl = p2 - p1
            cp = 2
        else:
            cl = 0
            cp = 1
        if cl > l:
            l = cl
            w = cp

    print w, l
