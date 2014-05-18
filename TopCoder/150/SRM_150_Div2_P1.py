import math


class WidgetRepairs:

    def days(self, arrivals, numPerDay):
        csum = 0
        days = 0
        for a in arrivals:
            csum += a
            if csum > 0:
                days += 1
            csum = 0 if csum < numPerDay else csum - numPerDay

        days += int(math.ceil(float(csum) / numPerDay))

        return days

if __name__ == "__main__":
    t = WidgetRepairs()
    print t.days((100, 100), 10)
    print t.days((10, 0, 0, 4, 20), 8)
