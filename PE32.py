l = list(range(1,10))
fin = []
for i in range(1,100):
    for j in range(111,10000):
        s = ''
        a = i*j
        s1 = str(i) + ',' + str(j) + ',' + str(a)
        s += str(i) + str(j) + str(a)
        for k in l:
            if str(k) not in s:
                break
            elif s.count(str(k)) > 1:
                break
            if len(s) > 9:
                break
        else:
            if a not in fin:
                fin.append(a)

print(sum(fin))