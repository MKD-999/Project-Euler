from decimal import Decimal, getcontext
from time import time as t

strt = t()

getcontext().prec = 105  # To ensure rounding does not affect the answer
ans = 0

for i in range(1, 101):

    if (int(i ** 0.5)) ** 2 != i:

        res = str(Decimal(i).sqrt())

        res = list(res)
        res.pop(1)

        res = res[:100]

        count = 0

        for j in res:
            count += int(j)

        ans += count

print(ans)
end = t()
print("------- %s seconds -------" % (end - strt))
