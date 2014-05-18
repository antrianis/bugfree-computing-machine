
class PairGameEasy:

    def __init__(self):
        self.dict = dict()

    def helper(self, a, b , c ,d):
        k = str(a) + '_' +str(b)
        if k in self.dict:
            return self.dict[k]

        if a == c and b == d:
            self.dict[k]  = 1
            return 1
        elif a > c or b > d:
            self.dict[k] = 0
            return 0

        if self.helper(a,b+a,c,d):
            return 1
        if self.helper(a+b,b,c,d):
            return 1
        return 0

        #return self.helper(a,b+a,c,d) or self.helper(a+b,b,c,d)



    def able(self, a , b, c , d):

       if  self.helper(a,b,c,d) == 1:
           return  "Able to generate"
       else:
           return "Not able to generate"



if __name__ == "__main__":
    t = PairGameEasy()

    print t.able(1,1,1000,1000)
    print t.able(1,2,3,5)
    print t.able(1,2,2,1)
    print t.able(2,2,2,999)
    print t.able(2,2,2,1000)
    print t.able(47,58,384,221)
    print t.able(1000,1000,1000,1000)
