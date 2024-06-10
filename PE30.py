i = 1000
l = []
while True:
    val = 0
    for j in list(str(i)):
        a = int(j)
        val += (a**5)
    if val == i:
        l.append(i)
    i += 1

    if len(l) == 6:
        break
print(sum(l))