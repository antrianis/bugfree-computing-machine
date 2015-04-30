def collatz(n):
    c = 0
    while n != 1:
        if n % 2:
            n = n*3 + 1
        else:
            n = n / 2
        c+=1
    return c
