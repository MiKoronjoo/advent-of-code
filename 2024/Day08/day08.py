import sys
from collections import defaultdict

city = sys.stdin.read().split()
antennas = defaultdict(list)
for i in range(len(city)):
    for j in range(len(city[0])):
        if (freq := city[i][j]) != '.':
            antennas[freq].append((i, j))

antinodes1 = set()
antinodes2 = set()
for i in range(len(city)):
    for j in range(len(city[0])):
        if (freq := city[i][j]) != '.':
            for x, y in antennas[freq]:
                if (x, y) != (i, j):
                    dx = x - i
                    dy = y - j
                    if 0 <= x + dx < len(city) and 0 <= y + dy < len(city[0]):
                        antinodes1.add((x + dx, y + dy))
                    while 0 <= x < len(city) and 0 <= y < len(city[0]):
                        antinodes2.add((x, y))
                        x += dx
                        y += dy
print(len(antinodes1))
print(len(antinodes2))
