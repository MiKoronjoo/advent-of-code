import sys

topographic = [list(row) for row in sys.stdin.read().split()]


def neighbors(x, y):
    n = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]
    return ((nx, ny) for nx, ny in n if 0 <= nx < len(topographic) and 0 <= ny < len(topographic[0]))


def run(x, y, val='0'):
    if val == '9':
        if (x, y) not in visited:
            visited.append((x, y))
            return 1, 1
        return 0, 1
    n_val = chr(ord(val) + 1)
    a1 = a2 = 0
    for nx, ny in neighbors(x, y):
        if topographic[nx][ny] == n_val:
            b1, b2 = run(nx, ny, n_val)
            a1 += b1
            a2 += b2
    return a1, a2


visited = []
ans1 = ans2 = 0
for i in range(len(topographic)):
    for j in range(len(topographic[0])):
        if topographic[i][j] == '0':
            br1, br2 = run(i, j)
            ans1 += br1
            ans2 += br2
            visited.clear()
print(ans1)
print(ans2)
