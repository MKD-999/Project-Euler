from time import time as t


# Default algo
def farey(n: int) -> int:
    a, b, c, d = 0, 1, 1, n
    cnt = 0

    while c <= n:

        k = (n + b) // d
        p = k * c - a
        q = k * d - b

        if (1 / 3) < a / b < (1 / 2):
            cnt += 1

        a, b, c, d = c, d, p, q

    return cnt


# Much better algo
def mod_farey(a: int, b: int, c: int, d: int, n: int) -> int:
    cnt = 0

    dup_c = c
    dup_d = d

    c += ((n - d) // b) * a
    d += ((n - d) // b) * b

    while c != dup_c and d != dup_d:
        k = (n + b) // d
        p = k * c - a
        q = k * d - b

        cnt += 1

        a, b, c, d = c, d, p, q

    return cnt


strt = t()
print(farey(12000))
end = t()
print("------- %s seconds -------" % (end - strt))

strt = t()
print(mod_farey(1, 3, 1, 2, 12000))
end = t()
print("------- %s seconds -------" % (end - strt))
