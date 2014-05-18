
class CandidatesSelectionEasy:

    def sort(self, score , x):
        indexscore = []
        index = []
        i = 0
        for s in score:
            indexscore.append(s[x])
            index.append(i)
            i+=1
        indexscore, index = zip(*sorted(zip(indexscore,index),key=lambda pair : pair[0]))

        return index
if __name__ == "__main__":
    t = CandidatesSelectionEasy()

    print t.sort(("ACB", "BAC", "CBA"),1)
