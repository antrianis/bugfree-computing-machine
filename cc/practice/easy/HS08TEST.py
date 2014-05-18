

if __name__ == '__main__':

    [w, i] = raw_input().split()

    w = int(w)
    i = float(i)

    if w % 5 == 0 and (i - w - 0.5) >= 0:
        print "%.2f" % (i - w - 0.5)
    else:
        print "%.2f" % i
