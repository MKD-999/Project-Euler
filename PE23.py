def abundant(a):
    s = 0
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            s += i
            val = a//i
            if val != i:
                s += val
    if s > a:
        return 'A'

l = []
for i in range(12,28111):
    a = abundant(i)
    if a == 'A':
      l.append(i)


final = set()

for i in range(len(l)):
    for j in range(i,len(l)):
        val = l[i] + l[j]
        if val < 28124:
            final.add(val)

s = set(range(1,28124))
print(sum(s.difference(final)))

