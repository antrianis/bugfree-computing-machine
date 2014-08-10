
if __name__ == '__main__':

    n,m=map(int,raw_input().split())
    lPoint = map(int,raw_input().split())
    print lPoint
    lPoint = sorted(enumerate(lPoint),key=lambda x:x[1])
    print lPoint
    lAns = [-1] * n
    x=0
    for i,t in lPoint:
        lAns[i]=x
        x^=1
        print x
    print " ".join(map(str,lAns))


def one():
    R=lambda:map(int,raw_input().split())
    n,m=R()
    a=zip(sorted(zip(R(),range(n))),[0,1]*n)
    print "a",a
    print ' '.join(map(str,map(lambda x:x[1],sorted(map(lambda x:(x[0][1],x[1]),a)))))
