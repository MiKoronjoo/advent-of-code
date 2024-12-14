import sys
import re


def print_tiles():
    print('\n'.join(''.join('.' if c == 0 else str(c) for c in t) for t in tiles))


def check_christmas_tree():
    for i in range(TALL):
        if '1111111111' in ''.join(map(str, tiles[i])):
            return True


WIDE = 101
TALL = 103
robots = [list(map(int, match.groups())) for match in re.finditer(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', sys.stdin.read())]
tiles = [WIDE * [0] for _ in range(TALL)]
for x, y, _, _ in robots:
    tiles[y][x] += 1

ranges = (
    (0, WIDE // 2, 0, TALL // 2), (WIDE // 2 + 1, WIDE, 0, TALL // 2),
    (0, WIDE // 2, TALL // 2 + 1, TALL), (WIDE // 2 + 1, WIDE, TALL // 2 + 1, TALL)
)

for sec in range(10000):
    for robot in robots:
        px, py, vx, vy = robot
        tiles[py][px] -= 1
        px += vx
        px %= WIDE
        py += vy
        py %= TALL
        tiles[py][px] += 1
        robot[0] = px
        robot[1] = py
    if check_christmas_tree():
        print_tiles()
        print('Part2:', sec + 1)
        if sec > 99:
            break
    if sec == 99:
        ans1 = 1
        for w0, w1, t0, t1 in ranges:
            ans1 *= sum(tiles[y][x] for x in range(w0, w1) for y in range(t0, t1))
        print('Part1:', ans1)
