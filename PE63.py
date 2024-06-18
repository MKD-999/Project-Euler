cnt = 0

for i in range(1,10):
    for j in range(1,100):
        if len(str(i**j)) == j:
            cnt += 1
print(cnt)