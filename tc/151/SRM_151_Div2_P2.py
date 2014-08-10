

class Birthday:

    def getDate(self, m, d):
        fdate = ""
        if m < 10:
            fdate += "0" + str(m) + "/"
        else:
            fdate += str(m) + "/"

        if d < 10:
            fdate += "0" + str(d)
        else:
            fdate += str(d)
        return fdate

    def getNext(self, date, birthdays):
        months = []
        days = []

        for b in birthdays:
            month = int(b.split()[0].split("/")[0])
            day = int(b.split()[0].split("/")[1])
            months.append(month)
            days.append(day)
        months, days = zip(*sorted(zip(months,days),key=lambda pair : pair[1]))
        months, days = zip(*sorted(zip(months,days),key=lambda pair : pair[0]))

        cm = int(date.split("/")[0])
        cd = int(date.split("/")[1])
        for i in range(len(months)):
            print months[i], days[i]
            if months[i] > cm or (months[i] == cm and days[i]>=cd):
                return self.getDate(months[i],days[i])
        return self.getDate(months[0],days[0])

if __name__ == "__main__":
    t = Birthday()
    # print t.getNext("06/17",("02/17 Wernie", "10/12 Stefan"))
    print t.getNext("09/13",("09/14 Wernie", "09/13 Stefan"))
