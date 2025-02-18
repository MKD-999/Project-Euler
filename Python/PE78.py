# Tried using previous algo, but it was too slow
# So had to look up recursion method by using pentagonal numbers
# Instead of using a recursive function, we use a list to store previous values

import itertools
from time import time as t

strt = t()

l = [1]  # p(0)

for i in itertools.count(len(l)):
    val = 0
    for j in itertools.count(1):

        if j % 2 == 0:
            sign = -1
        else:
            sign = 1

        pentagonal = (3 * (j ** 2) - j) // 2  # Generalised pentagonal numbers with +ve numbers
        if pentagonal <= i:
            val += sign * l[i - pentagonal]

        else:
            break

        if pentagonal + j <= i:  # Generalised pentagonal numbers with -ve numbers
            val += sign * l[i - pentagonal - j]

        else:
            break

    val %= 10 ** 6
    if val == 0:
        print(i)
        break
    l.append(val)

end = t()
print("------- %s seconds -------" % (end - strt))
