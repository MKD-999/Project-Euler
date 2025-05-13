val = 1
d = 2
s = 0
for k in range(500):
    if k == 0:
        for i in range(val,(val+4*d)+1,d):
            s += i
        d += 2
        val = i+d

    else:
        for i in range(val,(val+3*d)+1,d):
            s += i
        d += 2
        val = i+d
print(s)
