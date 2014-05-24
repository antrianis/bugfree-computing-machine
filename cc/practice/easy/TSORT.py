import sys

if __name__ == '__main__':
    nums = []
    t = int(raw_input())
    nums = map(int,sys.stdin.readlines())

    nums = sorted(nums)
    for n in nums:
        print n

