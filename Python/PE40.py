s = ''
for i in range(1,185186):
    s += str(i)
tochk = 1
ans = 1
while tochk <= 1000000:
    ans *= int(s[tochk-1])
    tochk *= 10
print(ans)