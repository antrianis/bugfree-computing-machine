

if __name__ == '__main__':

    t = int(raw_input())
    for k in range(t):
        colors,price = [],[]
        n,m = map(int,raw_input().split())
        for i in range(n):
            c,p = map(int,raw_input().split())
            colors.append(c)
            price.append(p)
        c, p = (list(x) for x in zip(*sorted(zip(colors, price), key=lambda pair: pair[0])))

        tsum = 0
        found = 0
        for i in range(n):
            if found == m:
                break
            tsum+=price[i]
            found+=1
            while(i + 1 < n and colors[i+1] == colors[i]):
                i+=1
        print tsum

