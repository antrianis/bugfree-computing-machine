
if __name__ == '__main__':
    chome, caway = {}, []
    teams = int(raw_input())

    for i in xrange(teams):
        h, a = map(int, raw_input().split())
        if h in chome:
            chome[h] += 1
        else:
            chome[h] = 1
        caway.append(a)

    opponents = teams - 1
    for t in xrange(teams):
        samecolor = 0 if not caway[t] in chome else chome[caway[t]]
        print (opponents + samecolor),  (opponents - samecolor)
