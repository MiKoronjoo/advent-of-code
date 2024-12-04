import sys


def coor0(n, m):
    return [[(i, j) for j in range(m)] for i in range(n)] + [[(i, j) for i in range(m)] for j in range(n)]


def coor1(n, m):
    return [[(a, j + a) for a in range(min(m - j, n))] for j in range(m - 1, -1, -1)] + [
        [(i + a, a) for a in range(n - i)] for i in range(1, n)]


def coor2(n, m):
    return [[(a, j - a) for a in range(min(j + 1, n))] for j in range(m)] + [
        [(i + a, m - 1 - a) for a in range(n - i)] for i in range(1, n)]


inp = sys.stdin.read().split('\n')

ans1 = 0
for goal in ('XMAS', 'SAMX'):
    for coor in (coor0, coor1, coor2):
        for ds in coor(len(inp), len(inp[0])):
            word = ''
            for x, y in ds:
                ch = inp[x][y]
                if ch == goal[len(word)]:
                    word += ch
                elif ch == goal[0]:
                    word = ch
                else:
                    word = ''
                if word == goal:
                    ans1 += 1
                    word = ''
print(ans1)


def char(x, y):
    if 0 <= x < len(inp) and 0 <= y < len(inp[0]):
        return inp[x][y]
    return '_'


ans2 = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == 'A':
            lu = char(i - 1, j - 1)
            rd = char(i + 1, j + 1)
            ru = char(i - 1, j + 1)
            ld = char(i + 1, j - 1)
            ans2 += lu + rd in 'MSM' and ru + ld in 'MSM'
print(ans2)
