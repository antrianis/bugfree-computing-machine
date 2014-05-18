import re

class FormatAmt:
    def amount(self, dollars, cents):
        d = ','.join(map(lambda e: e[::-1], re.findall(r'.{1,3}', str(dollars)[::-1]))[::-1])
        return '$' + d + '.' + (str(cents) if cents > 9 else  '0' + str(cents))



if __name__ == "__main__":
    t = FormatAmt()

    print t.amount(120345,1)
