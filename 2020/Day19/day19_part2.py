import random


def rec(pat, i):
    if i >= len(ss):
        return 0
    if type(pat) == str:
        return pat == ss[i]
    elif type(pat) == tuple:
        c = list(filter(bool, (rec(pos, i) for pos in pat)))
        if not c:
            return 0
        return random.choice(c)
    elif type(pat) == list:
        j = i
        for g in pat:
            res = rec(g, i)
            if not res:
                return 0
            i += res
        return i - j


a, b = open('inp19').read().strip().replace(
    '8: 42', '8: 42 | 42 8').replace('11: 42 31', '11: 42 31 | 42 11 31').split('\n\n')
rules = {}
for g in a.split('\n'):
    n, r = g.split(': ')
    if '"' in r:
        rules[n] = r.strip('"')
    else:
        rules[n] = tuple(g.split() for g in r.split(' | '))
for n, rr in rules.items():
    for r in rr:
        for i in range(len(r)):
            if r[i].isdigit():
                r[i] = rules[r[i]]
ans = 0
for ss in b.split('\n'):
    for _ in range(120):
        if rec(rules['0'], 0) == len(ss):
            ans += 1
            break
print(ans)
