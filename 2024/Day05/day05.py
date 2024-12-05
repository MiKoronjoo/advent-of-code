import sys
from collections import defaultdict

rs, us = sys.stdin.read().split('\n\n')
updates = [list(map(int, u.split(','))) for u in us.split()]
rules = defaultdict(list)
for r in rs.split():
    n1, n2 = map(int, r.split('|'))
    rules[n1].append(n2)

ans1 = ans2 = 0
for up in updates:
    lost_virginity = False
    for i in range(len(up)):
        next_nums = rules[up[i]]
        k = i
        for j in range(i - 1, -1, -1):
            if up[j] in next_nums:
                up[j], up[k] = up[k], up[j]
                k = j
                lost_virginity = True

    if lost_virginity:
        ans2 += up[len(up) // 2]
    else:
        ans1 += up[len(up) // 2]

print(ans1)
print(ans2)
