import math
#1034 2
#4,3 3,2 1,0 0,1

if __name__ == '__main__':

    n,k = map(int,raw_input().split())

    odigits = [int(char) for char in str(n)]
    digits = [(e,i) for i,e in enumerate(odigits)]
    digits.sort(key=lambda x : [x[0],-x[1]],reverse=True)
    print digits
    o = 0

    for e,i in digits:
        if (i - o) <= k:
            temp = odigits[o]
            odigits[o] = odigits[i]
            odigits[i] = temp
            k-=i
            k+=1
            o+=1
        if k <= 0:
            break
    print "" + "".join((map(str,odigits)))
