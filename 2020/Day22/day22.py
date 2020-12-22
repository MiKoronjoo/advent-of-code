def game(d1, d2):
    prv = set()
    while d1 and d2:
        e1 = '-'.join(map(str, d1))
        e2 = '-'.join(map(str, d2))
        if e1 in prv or e2 in prv:
            return True
        else:
            prv.update((e1, e2))
        if len(d1) - 1 >= d1[0] and len(d2) - 1 >= d2[0]:
            if game(d1[1:d1[0] + 1], d2[1:d2[0] + 1]):
                d1 += [d1.pop(0), d2.pop(0)]
            else:
                d2 += [d2.pop(0), d1.pop(0)]
        elif d1[0] > d2[0]:
            d1 += [d1.pop(0), d2.pop(0)]
        else:
            d2 += [d2.pop(0), d1.pop(0)]
    return bool(d1)


p1, p2 = open('inp22').read().strip().split('\n\n')
deck1 = list(map(int, p1.split('\n')[1:]))
deck2 = list(map(int, p2.split('\n')[1:]))
d1 = deck1.copy()
d2 = deck2.copy()
while d1 and d2:
    if d1[0] > d2[0]:
        d1 += [d1.pop(0), d2.pop(0)]
    else:
        d2 += [d2.pop(0), d1.pop(0)]
print(sum(i * n for i, n in enumerate(reversed(d1 or d2), 1)))
game(deck1, deck2)
print(sum(i * n for i, n in enumerate(reversed(deck1 or deck2), 1)))
