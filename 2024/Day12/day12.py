import sys


def neighbors(x, y):
    label = garden[x][y][0]
    return [(nx, ny) for nx, ny in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y))
            if 0 <= nx < len(garden) and 0 <= ny < len(garden[0]) and garden[nx][ny][0] == label]


def sides(x, y):
    n = [
        (x - 1, y - 1, '1'), (x - 1, y, '2'), (x - 1, y + 1, '3'),
        (x, y - 1, '4'), (x, y + 1, '6'),
        (x + 1, y - 1, '7'), (x + 1, y, '8'), (x + 1, y + 1, '9')
    ]
    label = garden[x][y][0]
    nn = tuple(d for nx, ny, d in n
               if 0 <= nx < len(garden) and 0 <= ny < len(garden[0]) and garden[nx][ny][0] == label)
    res = 0
    res += ('2' in nn and '4' in nn and '1' not in nn) or ('2' not in nn and '4' not in nn)
    res += ('2' in nn and '6' in nn and '3' not in nn) or ('2' not in nn and '6' not in nn)
    res += ('4' in nn and '8' in nn and '7' not in nn) or ('4' not in nn and '8' not in nn)
    res += ('6' in nn and '8' in nn and '9' not in nn) or ('6' not in nn and '8' not in nn)
    return res


def iterate(x, y):
    garden[x][y][1] = True
    pp = 4
    aa = 1
    ss = sides(x, y)
    for nx, ny in neighbors(x, y):
        pp -= 1
        if not garden[nx][ny][1]:
            da, dp, ds = iterate(nx, ny)
            pp += dp
            aa += da
            ss += ds
    return aa, pp, ss


garden = [[[label, False] for label in row] for row in sys.stdin.read().split()]

ans1 = ans2 = 0
for i in range(len(garden)):
    for j in range(len(garden[0])):
        if not garden[i][j][1]:
            area, perimeter, side = iterate(i, j)
            ans1 += area * perimeter
            ans2 += area * side

print(ans1)
print(ans2)
