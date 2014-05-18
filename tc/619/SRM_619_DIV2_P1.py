class GoodCompanyDivTwo:

    def countGood(self, superior, workType):
        diverse = 0
        for i in range(0,len(superior)):
            dep = []
            dep.append(workType[i])
            for j in range(i,len(superior)):
                if superior[j] == i:
                    dep.append(workType[j])
            if len(dep) == len(set(dep)):
                diverse+=1

        return diverse

if __name__ == "__main__":
    t = GoodCompanyDivTwo()
    print  t.countGood((-1,0), (1,2))
    print t.countGood(
        (-1, 0, 1, 0, 0),
        (3, 3, 5, 2, 2))
