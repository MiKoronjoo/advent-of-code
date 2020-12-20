tts = []
sides = []
for tinfo in open('inp20').read().strip().split('\n\n'):
    fl, *tile = tinfo.split('\n')
    tid = int(fl[5:-1])
    edges = [tile[0], tile[-1], ''.join(c for c, *_ in tile), ''.join(c for *_, c in tile)]
    sides.extend(edges)
    tts.append((tid, edges))
# part 1
ans = 1
for tid, edges in tts:
    if sum(sides.count(e) + sides.count(e[::-1]) == 2 for e in edges) == 2:
        ans *= tid
print(ans)
