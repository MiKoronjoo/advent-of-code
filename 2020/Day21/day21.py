from functools import reduce

alrg = {}
alls = []
for food in open('inp21').read().strip().split('\n'):
    a, b = food.split(' (contains ')
    ingredients = set(a.split())
    alls.extend(ingredients)
    allergens = b[:-1].split(', ')
    for ag in allergens:
        if ag not in alrg:
            alrg[ag] = ingredients.copy()
        else:
            alrg[ag].intersection_update(ingredients)
np = reduce(lambda x, y: x.union(y), alrg.values())
print(sum(1 for x in alls if x not in np))
res = {}
while alrg:
    k, v = min(alrg.items(), key=lambda x: len(x[1]))
    alrg.pop(k)
    for st in alrg.values():
        st.difference_update(v)
    res[k] = v.pop()
print(','.join(str(y[1]) for y in sorted(res.items(), key=lambda x: x[0])))
