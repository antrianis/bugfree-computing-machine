import os
import random
f = open("sample.txt","w")
lineno=random.randint(0,1000000)
divisor=random.randint(0,10000000)
f.write(str(lineno) + " " + str(divisor) + "\n")
for i in range(0,lineno):
    f.write(str(random.randint(0,1000000000)) + "\n")
f.close()
