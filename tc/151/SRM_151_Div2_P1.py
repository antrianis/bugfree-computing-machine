import math


class PrefixCode:

    def isOne(self, words):
        no = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if words[j].startswith(words[i]):
                        no.append(i)

        if len(no) > 0:
            no.sort()
            return "No, " + str(no[0])
        else:
            return "Yes"

if __name__ == "__main__":
    t = PrefixCode()
    print t.isOne(("hello"))
    #print t.days((10, 0, 0, 4, 20), 8)
