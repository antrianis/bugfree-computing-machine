import math

if __name__ == '__main__':

    n,m = map(int,raw_input().split())
    a = map(int,raw_input().split())

    i = 0
    buses = 0
    while(i<n):
        free = m - a[i]
        i+=1
        buses+=1
        while(i < n and a[i] <= free):
            free = free - a[i]
            i+=1

    print buses
