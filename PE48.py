from time import time

strt = time()
fin = 0
for j in range(1,1001):

    x = (j**j) #% (10**10)
    fin += x

print(str(fin)[-10:])
fin = time()
print(fin-strt)