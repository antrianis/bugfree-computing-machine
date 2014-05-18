if __name__ == '__main__':

    t = int(raw_input())
    one_hole = ('A', 'D', 'O','Q', 'P', 'R')
    two_hole = ('B')
    for i in range(t):
        count = 0
        w = str(raw_input())
        for l in w:
            if l in one_hole:
                count += 1
            elif l in two_hole:
                count += 2
        print count
