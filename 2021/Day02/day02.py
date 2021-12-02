import sys

h = d1 = 0
a2 = d2 = 0
for c in sys.stdin.readlines():
    n = int(c.split()[1])
    h += c[0] == 'f' and n
    d1 += c[0] == 'd' and n
    d1 -= c[0] == 'u' and n

    a2 += c[0] == 'd' and n
    a2 -= c[0] == 'u' and n
    d2 += c[0] == 'f' and n * a2

print(h * d1)
print(h * d2)
