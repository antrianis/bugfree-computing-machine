def isPal(n):
    i = 0
    j = len(n) -1

    while (i <= j):
        if n[i] != n[j]:
            break
        i+=1
        j-=1
    if i <= j:
        return False
    return True

def isPrime(n):
    for i in range(2,n-1):
        if n

if __name__ == '__main__':

    r = int(raw_input())
    while(true):

        if isPal(str(r)) and isPrime(str(n)):
            print r
            break
        r+=1
