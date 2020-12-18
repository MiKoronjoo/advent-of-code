class N:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return N(self.num + other.num)

    def __sub__(self, other):
        return N(self.num * other.num)


class M:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return M(self.num * other.num)

    def __mul__(self, other):
        return M(self.num + other.num)


inp = open('inp18').read().strip().replace('*', '-')
for d in '0123456789':
    inp = inp.replace(d, f'N({d})')
print(sum(eval(line).num for line in inp.split('\n')))
print(sum(eval(line).num for line in inp.replace('+', '*').replace('-', '+').replace('N', 'M').split('\n')))
