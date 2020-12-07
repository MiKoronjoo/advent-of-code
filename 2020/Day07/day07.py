from collections import defaultdict


def part1(ch):
    res = 0
    for par in parents[ch]:
        if not par[1]:
            par[1] = True
            res += 1 + part1(par[0])
    return res


def part2(par):
    res = 0
    for ch, n in children[par]:
        res += n + n * part2(ch)
    return res


parents = defaultdict(list)
children = defaultdict(list)
for rule in open('inp07').readlines():
    rps = rule.split()
    pname = ' '.join(rps[:2])
    parent = [pname, False]
    n = rps[4]
    if n != 'no':
        child = ' '.join(rps[5:7])
        parents[child].append(parent)
        children[pname].append((child, int(n)))
        i = 7
        while rps[i][-1] == ',':
            child = ' '.join(rps[i + 2:i + 4])
            parents[child].append(parent)
            children[pname].append((child, int(rps[i + 1])))
            i += 4

bag = 'shiny gold'
print(part1(bag))
print(part2(bag))
