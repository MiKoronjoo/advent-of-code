a, b, c = open('inp16').read().strip().split('\n\n')
ranges = {}
for r in a.split('\n'):
    name, rng = r.replace(' or ', '-').split(': ')
    ranges[name] = tuple(map(int, rng.split('-')))
my_tic = list(map(int, b.split('\n')[1].split(',')))
nr_tic = [list(map(int, l.split(','))) for l in c.split('\n')[1:]]
res = []
for x in sum(nr_tic, []):
    for r in ranges.values():
        if r[0] <= x <= r[1] or r[2] <= x <= r[3]:
            break
    else:
        res.append(x)
print(sum(res))
for x in res:
    for t in nr_tic:
        if x in t:
            nr_tic.remove(t)
            break
nr_tic.append(my_tic)
d = {}
for i in range(len(my_tic)):
    column = [t[i] for t in nr_tic]
    d[i] = [name for name, r in ranges.items()
            if next((0 for num in column if not (r[0] <= num <= r[1] or r[2] <= num <= r[3])), 1)]
res2 = 1
while d:
    k, v = min(d.items(), key=lambda x: len(x[1]))
    name = v[0]
    if name.startswith('departure'):
        res2 *= my_tic[k]
    for l in d.values():
        if name in l:
            l.remove(name)
    d.pop(k)
print(res2)
