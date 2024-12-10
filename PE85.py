from time import time as t


def rectangles(a: int, b: int) -> int:

    part1 = (a * (a + 1)) // 2
    part2 = (b * (b + 1)) // 2

    return part1 * part2


start = t()

chk = 2_000_000
ans = 0

for i in range(50, 1001):
    for j in range(10, 60):

        if rectangles(i, j) > 3_000_000:
            break

        else:
            if abs(2_000_000 - rectangles(i, j)) < chk:
                chk = abs(2_000_000 - rectangles(i, j))
                ans = i * j

print(ans)
end = t()
print('------- %s seconds -------' % (end - start))
