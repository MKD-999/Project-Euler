s = '123456789'

fin_val = 0
length = 0

for i in range(9,10000000):
    n = 1
    val = ''
    while len(val) < 9:
        a = str(i * n)
        val += a
        n += 1

    length = n-1
    for j in val:
        if val.count(j) > 1:
            length = 0
            break

    for k in val:
        if k not in s:
            length = 0
            break

    if length != 0:
        print(val)













