
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

if __name__ == '__main__':
    t = int( raw_input())
    for i in range(t):
        n = int(raw_input())
        print factorial(n)


