from time import time as t

strt = t()


def mask(a, b, c, d, e, f, g, h, i, j):
    outer = [a, h, i, j, g]

    ind = outer.index(min(outer))
    final = outer[ind:] + outer[:ind]

    nums = {a: [b, c],
            h: [c, d],
            g: [f, b],
            j: [e, f],
            i: [d, e]
            }

    s = ''
    for some in final:

        toappend = str(some)

        for thng in nums[some]:
            toappend += str(thng)

        s += toappend

    return s


l = []

nums = list(range(1, 11))

for a in nums:

    b_nums = nums[:]
    b_nums.remove(a)

    for b in b_nums:

        c_nums = b_nums[:]
        c_nums.remove(b)

        for c in c_nums:

            d_nums = c_nums[:]
            d_nums.remove(c)

            for d in d_nums:

                e_nums = d_nums[:]
                e_nums.remove(d)

                for e in e_nums:

                    f_nums = e_nums[:]
                    f_nums.remove(e)

                    for f in f_nums:

                        total = a + b + c
                        g_nums = f_nums[:]
                        g_nums.remove(f)

                        g = total - f - b
                        if g in g_nums:

                            h_nums = g_nums[:]
                            h_nums.remove(g)

                            h = total - c - d
                            if h in h_nums:

                                i_nums = h_nums[:]
                                i_nums.remove(h)

                                i = total - d - e

                                if i in i_nums:

                                    j_nums = i_nums[:]
                                    j_nums.remove(i)

                                    j = total - e - f
                                    if j in j_nums:
                                        l.append(mask(a, b, c, d, e, f, g, h, i, j))

print(max(l) if len(max(l)) == 16 else 0)
end = t()
print(end - strt)
