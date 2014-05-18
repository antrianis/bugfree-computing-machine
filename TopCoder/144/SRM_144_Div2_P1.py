
class Time:

    # def whatTime(self, seconds):
    #     hours = seconds / 3600
    #     min = (seconds - hours * 3600) / 60
    #     sec = (seconds - hours * 3600 - min * 60 )
    #     return str(hours) +  ":" + str(min) + ":" + str(sec)

    def whatTime(self, seconds):
        return "{}:{}:{}".format(seconds/3600, (seconds%3600)/60, (seconds%60))

if __name__ == "__main__":
    t = Time()
    assert t.whatTime(0) == "0:0:0"
    print t.whatTime(3661)
    print t.whatTime(5436)
    print t.whatTime(86399)
