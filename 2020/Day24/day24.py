move = {
    'e': lambda pos: (pos[0] + 2, pos[1]),
    'w': lambda pos: (pos[0] - 2, pos[1]),
    'ne': lambda pos: (pos[0] + 1, pos[1] + 1),
    'nw': lambda pos: (pos[0] - 1, pos[1] + 1),
    'se': lambda pos: (pos[0] + 1, pos[1] - 1),
    'sw': lambda pos: (pos[0] - 1, pos[1] - 1)
}
blacks = []
for line in open('inp24').read().split():
    pv = ''
    pos = (0, 0)
    for c in line:
        if c in 'ew':
            i = (pv + c).lstrip('ew') or c
            pos = move[i](pos)
        pv = c
    if pos in blacks:
        blacks.remove(pos)
    else:
        blacks.append(pos)
print(len(blacks))

tiles = {b: [True, None] for b in blacks}
missed = []
for _ in range(100):
    for t in list(tiles.keys()):
        for m in move.values():
            adj = m(t)
            if adj not in tiles:
                tiles[adj] = [False, None]
    for t, color in tiles.items():
        blk = 0
        for m in move.values():
            adj = m(t)
            if adj not in tiles:
                missed.append(adj)
                continue
            blk += tiles[adj][0]
            if blk > 2:
                break
        if color[0] and (blk == 0 or blk > 2):
            color[1] = False
        elif not color[0] and blk == 2:
            color[1] = True
    for color in tiles.values():
        if color[1] is not None:
            color[0] = color[1]
            color[1] = None
    tiles.update((adj, [False, None]) for adj in missed)
    missed.clear()
print(sum(c[0] for c in tiles.values()))
