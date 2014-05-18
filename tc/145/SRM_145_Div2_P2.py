
class ExerciseMachine:

    def getPercentages(self, time):
        count = 0
        secs = int(time[0:2])*3600 + int(time[3:5])*60 + int(time[6:8])
        for i in range(1, secs - 1):
            if (i * 100 / float(secs)) == int(i* 100 / float(secs)):
                count+=1
        return count

if __name__ == "__main__":
    t = ExerciseMachines()
    print t.getPercentages("00:30:00")
