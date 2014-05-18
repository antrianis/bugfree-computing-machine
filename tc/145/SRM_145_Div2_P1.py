
class ImageDithering:

    def count(self, dithered, screen):
        no = 0
        k = 0
        for row in screen:
            for i in range(0, len(row)):
                if row[i] in dithered:
                    no += 1
        return no

if __name__ == "__main__":
    t = ImageDithering()

    print t.count("BW",
                  ("AAAAAAAA",
                   "ABWBWBWA",
                   "AWBWBWBA",
                   "ABWBWBWA",
                   "AWBWBWBA",
                   "AAAAAAAA"))

    print t.count("BW",
                  ("BBBBBBBB",
                   "BBWBWBWB",
                   "BWBWBWBB",
                   "BBWBWBWB",
                   "BWBWBWBB",
                   "BBBBBBBB"))
