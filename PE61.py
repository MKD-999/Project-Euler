from time import time as t


def compat(*args):

    vals = {*args}
    from itertools import permutations as perm

    perms = perm(vals)
    for i in perms:
        s = ''
        for j in i:
            s += str(j)

        cnt = 3
        if len(vals) == 6:
            for k in range(len(vals)-1):

                if s[cnt-1:cnt+1] != s[cnt+1:cnt+3]:
                    break

                else:
                    cnt += 4

            else:
                m = ''
                for l in reversed(s[-1:-3:-1]):
                    m += l
                if s[:2] == m:
                    return i

        else:
            for k in range(len(vals)-1):

                if s[cnt-1:cnt+1] != s[cnt+1:cnt+3]:
                    break

                else:
                    cnt += 4

            else:
                return i


strt = t()
tri = []
sq = []
pent = []
hex = []
hept = []
oct = []

x = 1

while True:

    if len(str(x * (x + 1) // 2)) == 5:
        break

    elif len(str(x * (x + 1) // 2)) == 4:
        tri.append([x * (x + 1) // 2, x])
        x += 1

    else:
        x += 1

x = 1

while True:

    if len(str(x ** 2)) == 5:
        break

    elif len(str(x ** 2)) == 4:
        sq.append([x ** 2, x])
        x += 1
    else:
        x += 1

x = 1
while True:

    if len(str(x * (3 * x - 1) // 2)) == 5:
        break

    elif len(str(x * (3 * x - 1) // 2)) == 4:
        pent.append([x * (3 * x - 1) // 2, x])
        x += 1
    else:
        x += 1

x = 1
while True:

    if len(str(x * (2 * x - 1))) == 5:
        break

    elif len(str(x * (2 * x - 1))) == 4:
        hex.append([x * (2 * x - 1), x])
        x += 1

    else:
        x += 1

x = 1
while True:

    if len(str(x * (5 * x - 3) // 2)) == 5:
        break

    elif len(str(x * (5 * x - 3) // 2)) == 4:
        hept.append([x * (5 * x - 3) // 2, x])
        x += 1

    else:
        x += 1

x = 1
while True:

    if len(str(x * (3 * x - 2))) == 5:
        break

    elif len(str(x * (3 * x - 2))) == 4:
        oct.append([x * (3 * x - 2), x])
        x += 1

    else:
        x += 1




for x in oct:
    for y in hept:
        if compat(x[0],y[0]) != None:
            for z in hex:
                if compat(x[0],y[0],z[0]) != None:
                    for a in pent:
                        if compat(x[0], y[0], z[0],a[0]) != None:
                            for b in sq:
                                if compat(x[0], y[0], z[0], a[0],b[0]) != None:
                                    for c in tri:
                                        if compat(x[0], y[0], z[0], a[0], b[0],c[0]) != None:
                                            if len(compat(x[0], y[0], z[0], a[0], b[0],c[0])) == 6:
                                                if x[1] != y[-1] != z[-1] != a[-1] != b[-1] != c[-1]:
                                                    print(compat(x[0], y[0], z[0], a[0], b[0], c[0]))
                                                    print(x[1],y[1],z[1],a[1],b[1],c[1])
                                                    ans = 0
                                                    for d in compat(x[0], y[0], z[0], a[0], b[0], c[0]):
                                                        ans += d

                                                    print(ans)
                                        else:
                                            continue

                                else:
                                    continue

                        else:
                            continue

                else:
                    continue
        else:
            continue

end = t()
print(end-strt)