import time

strt = time.time()
l = []
for i in range(3,501):
    for j in range(i,501):
        k = int((i**2 + j**2)**0.5)
        if k**2 == i**2 + j**2:
                s = i+j+k
                if s <= 1000:
                    l.append(s)
fin = 0
ans = 0
for i in l:
    cnt = l.count(i)
    ind = l.index(i)
    if cnt > fin:
        fin = cnt
        ans = ind
print(l[ans])
fin = time.time()
print(fin-strt)



