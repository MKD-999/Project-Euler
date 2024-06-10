import math
ans = 0
for i in range(3,100000):
    s = 0
    a = str(i)
    for j in a:
        val = int(j)
        fin = math.factorial(val)
        s += fin
    if s == i:
        ans += i
print(ans)