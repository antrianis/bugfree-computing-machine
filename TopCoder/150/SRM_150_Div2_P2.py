import math


class InterestingDigits:

    def base(self, base):
        digitMaxLen = len(str(base-1))
        maxNum = str(base-1)
        while(len(maxNum) < 4 * digitMaxLen):
            maxNum+=maxNum

        for n in xrange(base):
            while (sum < int(maxNum)):
                print sum
        return maxNum
if __name__ == "__main__":
    t = InterestingDigits()
    print t.base(3)
    print t.base(10)
