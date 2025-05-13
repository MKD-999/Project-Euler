pents = []
for j in range(144,100000):
    b = (j*(3*j-1))//2
    pents.append(b)

hexs = []
for k in range(144,100000):
        c = k*(2*k-1)
        hexs.append(c)

for i in hexs:
    if i in pents:
            print(i)