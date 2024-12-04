import sys


def coor1(n, m):
    res = []
    for j in range(m - 1, -1, -1):
        d = []
        for a in range(min(m - j, n)):
            d.append((a, j + a))
        res.append(d)

    for i in range(1, n):
        d = []
        for a in range(n - i):
            d.append((i + a, a))
        res.append(d)
    return res


def coor2(n, m):
    res = []
    for j in range(m):
        d = []
        for a in range(min(j + 1, n)):
            d.append((a, j - a))
        res.append(d)

    for i in range(1, n):
        d = []
        for a in range(n - i):
            d.append((i + a, m - 1 - a))
        res.append(d)
    return res


inp = sys.stdin.read().split('\n')
t_inp = [''.join(x) for x in zip(*inp)]

ans1 = 0
for goal in ('XMAS', 'SAMX'):
    for ws in (inp, t_inp):
        for row in ws:
            word = ''
            for ch in row:
                if ch == goal[len(word)]:
                    word += ch
                elif ch == goal[0]:
                    word = ch
                else:
                    word = ''
                if word == goal:
                    ans1 += 1
                    word = ''

    for coor in (coor1, coor2):
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
