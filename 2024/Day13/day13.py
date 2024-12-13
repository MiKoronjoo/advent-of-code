import sys
import re

machines = (map(int, re.findall(r'\d+', raw_mach)) for raw_mach in sys.stdin.read().split('\n\n'))
ans1 = ans2 = 0
for ax, ay, bx, by, px, py in machines:
    for a in range(100):
        for b in range(100):
            x, y = ax * a + bx * b, ay * a + by * b
            if (x, y) == (px, py):
                ans1 += a * 3 + b
                break
        else:
            continue
        break

    px += 10 ** 13
    py += 10 ** 13
    # ax * a + bx * b = px
    # ay * a + by * b = py
    a0 = bx * py - by * px
    a1 = ay * bx - ax * by
    if a0 % a1 == 0:
        a = a0 // a1
        b0 = px - ax * a
        if b0 % bx == 0:
            b = b0 // bx
            ans2 += a * 3 + b
print(ans1)
print(ans2)
