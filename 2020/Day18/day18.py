N = type('N', (object,), {'__init__': (lambda s, n: s.__setattr__('n', n)),
                          '__add__': (lambda s, o: N(s.n + o.n)),
                          '__sub__': (lambda s, o: N(s.n * o.n))})
M = type('M', (object,), {'__init__': (lambda s, n: s.__setattr__('n', n)),
                          '__add__': (lambda s, o: M(s.n * o.n)),
                          '__mul__': (lambda s, o: M(s.n + o.n))})
inp = open('inp18').read().strip().replace('*', '-')
for d in '0123456789':
    inp = inp.replace(d, f'N({d})')
print(sum(eval(line).n for line in inp.split('\n')))
print(sum(eval(line).n for line in inp.replace('+', '*').replace('-', '+').replace('N', 'M').split('\n')))
