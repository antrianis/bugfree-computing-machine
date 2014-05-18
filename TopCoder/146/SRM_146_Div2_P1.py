
class YahtzeeScore:

    def maxPoints(self, toss):
        current_max = 0
        current_sum = 0
        toss = sorted(list(toss))
        current_sum = toss[0]

        for i in range(1, len(toss)):
            if toss[i] == toss[i - 1]:
                current_sum += toss[i]
            else:
                current_sum = toss[i]

            current_max = max(current_max, current_sum)
        return current_max

    def maxPoints(self,toss):
        return max(map(lambda i: i*toss.count(i), range(1,7)))

if __name__ == "__main__":
    t = YahtzeeScore()

    print t.maxPoints((2, 2, 3, 5, 4))
