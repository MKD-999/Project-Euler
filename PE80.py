from decimal import Decimal, getcontext

getcontext().prec = 105  # To ensure rounding does not affect the answer
ans = 0

for i in range(1, 101):

    if (int(i ** 0.5)) ** 2 != i:

        res = str(Decimal(i).sqrt())

        res = list(res)
        res.pop(1)

        for j in range(5, 0, -1):
            res.pop(-j)

        count = 0

        for j in res:
            count += int(j)

        ans += count

print(ans)

