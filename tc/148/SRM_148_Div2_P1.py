
class DivisorDigits:

    def howMany(self, number):
        count = 0
        n = number
        while (not number == 0 ):
            digit = number % 10
            if  digit != 0 and n % digit == 0:
                count+=1
            number/=10
        return count
if __name__ == "__main__":
    t = DivisorDigits()

    print t.howMany(120345)
