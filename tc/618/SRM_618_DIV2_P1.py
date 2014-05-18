

class WritingWords:

    def write(self, word):

        return sum(map(lambda c: ord(c) - 64, word))

if __name__ == "__main__":
    t = WritingWords()
    print  t.write("ABCD")
