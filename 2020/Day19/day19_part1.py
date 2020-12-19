import re


def to_re(ss):
    return str(ss).replace(', ', '').replace("'", '').replace('[', '(').replace(']', ')')


a, b = open('inp19').read().strip().split('\n\n')
rules = {}
for g in a.split('\n'):
    n, r = g.split(': ')
    if '"' in r:
        rules[n] = r.strip('"')
    else:
        rules[n] = r.split()
for n, r in rules.items():
    for i in range(len(r)):
        if r[i].isdigit():
            r[i] = rules[r[i]]

pat = to_re(rules['0'])
print(sum(1 for ss in b.split('\n') if re.match(f'^{pat}$', ss)))
