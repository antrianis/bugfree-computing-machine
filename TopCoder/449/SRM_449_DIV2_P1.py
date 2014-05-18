import math


class MountainRoad:

    def findDistance(self, start, finish):
        sq2 = math.sqrt(2)
        length = 0

        start, finish = zip(*sorted(zip(start,finish),key=lambda pair : pair[0]))

        for s, f in zip(start, finish):
            a = (f - s) / sq2
            length += (2 * a)
        for i in range(0, len(start) - 1):

            #remove overlapping sites
            if finish[i] > start[i + 1] and not finish[i+1] < finish[i]:
                a = (finish[i] - start[i + 1]) / sq2
                length -= (2 * a)

            #contained in another triangle remove all of it
            if start[i] < start[i + 1] and finish[i+1] < finish[i]:
                a = (finish[i+1] - start[i+1]) / sq2
                length -= (2 * a)
        return length


if __name__ == "__main__":
    t = MountainRoad()
    print "result", t.findDistance({1}, {7})
    print "result", t.findDistance((0, 3, 4), (5, 9, 6))
    print "result", t.findDistance((-5,-3),
                                   (-2,-2))
    print "result", t.findDistance((1, 4, 5, 6, -10), (101, 102, 101, 100, 99))
