
class CCipher:

    def decode(self, cipherText, shift):
        dec = ""
        for i in range(0, len(cipherText)):
            shifted = ord(cipherText[i]) - shift
            if shifted < 65:
                shifted = 90 - (65 % shifted)

            dec+=str(unichr(shifted))
        return dec

if __name__ == "__main__":
    t = CCipher()

    print t.decode("VQREQFGT",2)
