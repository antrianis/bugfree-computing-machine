import os
import random
f = open("tsort.txt","w")
total = 10000000
f.write(str(total) + "\n")
for i in range(0,total):
    f.write(str(random.randint(0,10000000)) + "\n")
f.close()
