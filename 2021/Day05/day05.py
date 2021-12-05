from collections import defaultdict


def line(x1, y1, x2, y2):
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            covers[(x1, y)][0] += 1
            covers[(x1, y)][1] += 1
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            covers[(x, y1)][0] += 1
            covers[(x, y1)][1] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        if x1 > x2:
            x1, x2, y1, y2 = x2, x1, y2, y1
        step = 1 if y1 < y2 else -1
        x = x1
        for y in range(y1, y2 + step, step):
            covers[(x, y)][1] += 1
            x += 1


covers = defaultdict(lambda: [0, 0])
while True:
    try:
        a, b = input().split(' -> ')
    except EOFError:
        break
    x1, y1 = map(int, a.split(','))
    x2, y2 = map(int, b.split(','))
    line(x1, y1, x2, y2)

print(sum(1 for c in covers.values() if c[0] > 1))
print(sum(1 for c in covers.values() if c[1] > 1))
