print(*(lambda covers: [(lambda a, b, covers: (lambda lst, covers: [covers.__setitem__((lst[0], y), [covers[(lst[0], y)][0] + 1, covers[(lst[0], y)][1] + 1]) for y in range(lst[1], lst[3] + (1 if lst[1] < lst[3] else -1), (1 if lst[1] < lst[3] else -1))] if lst[0] == lst[2] else [covers.__setitem__((x, lst[1]), [covers[(x, lst[1])][0] + 1, covers[(x, lst[1])][1] + 1]) for x in range(lst[0], lst[2] + (1 if lst[0] < lst[2] else -1), (1 if lst[0] < lst[2] else -1))] if lst[1] == lst[3] else [covers.__setitem__((lst[2], y), [covers[(lst[2], y)][0], covers[(lst[2], y)][1] + 1]) or lst.__setitem__(2, lst[2] + 1) for y in range(lst[3], lst[1] + (1 if lst[3] < lst[1] else -1), (1 if lst[3] < lst[1] else -1))] if lst[0] > lst[2] else [covers.__setitem__((lst[0], y), [covers[(lst[0], y)][0], covers[(lst[0], y)][1] + 1]) or lst.__setitem__(0, lst[0] + 1) for y in range(lst[1], lst[3] + (1 if lst[1] < lst[3] else -1), (1 if lst[1] < lst[3] else -1))] if abs(lst[0] - lst[2]) == abs(lst[1] - lst[3]) else [])([*map(int, a.split(',')), *map(int, b.split(','))], covers))(*inp.split(' -> '), covers) for inp in __import__('sys').stdin.read().strip().split('\n')] and (sum(1 for c in covers.values() if c[0] > 1), sum(1 for c in covers.values() if c[1] > 1)))(__import__('collections').defaultdict(lambda: [0, 0])), sep='\n')