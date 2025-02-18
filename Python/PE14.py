from time import time as t

strt = t()

lengths = [0] * 1000000
ans = 0
chk = 0

for i in range(2, 1000000):

    n = i
    count = 1
    while n != 1:

        try:
            if lengths[n] != 0:
                count += (lengths[n] - 1)
                break

            else:
                raise IndexError

        except IndexError:
            if n % 2 == 0:
                n //= 2
                count += 1
            else:
                n = 3 * n + 1
                count += 1

    lengths[i] = count
    if count > chk:
        chk = count
        ans = i

print(ans)
end = t()
print("------- %s seconds -------" % (end - strt))
