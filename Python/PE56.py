ans = 0
tochk = 99

for i in range(90,100):

    val = 0
    a = str(tochk**i)
    for j in a:
        val += int(j)

    if val > ans:
        ans = val
print(ans)

