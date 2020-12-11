from copy import deepcopy


def valid(i, j):
    return 0 <= i < len(MAP) and 0 <= j < len(MAP[0])


def adj(x, y, mp):
    return [mp[x + i][y + j] for i in range(-1, 2) for j in range(-1, 2) if (i or j) and valid(x + i, y + j)].count('#')


def occ(x, y, mp):
    res = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i or j:
                z = 1
                while valid(x + i * z, y + j * z):
                    st = mp[x + i * z][y + j * z]
                    if st == '.':
                        z += 1
                        continue
                    res += st == '#'
                    break
    return res


def calc(mp, f, n):
    temp = deepcopy(mp)
    while True:
        for x in range(len(mp)):
            for y in range(len(mp[0])):
                res = f(x, y, mp)
                if mp[x][y] == 'L':
                    if not res:
                        temp[x][y] = '#'
                elif mp[x][y] == '#':
                    if res > n:
                        temp[x][y] = 'L'
        if mp == temp:
            break
        mp = deepcopy(temp)
    return sum(mp, []).count('#')


MAP = [list(line) for line in open('inp11').read().split()]
print(calc(MAP, adj, 3), calc(MAP, occ, 4), sep='\n')
