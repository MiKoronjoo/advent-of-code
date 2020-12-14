def rec(num):
    if not num:
        return ['']
    if num[0] == 'X':
        return [x + n for n in rec(num[1:]) for x in '01']
    return [num[0] + n for n in rec(num[1:])]


mem = {}
lines = open('inp14').readlines()
for line in lines:
    var, val = line.split(' = ')
    if var == 'mask':
        mask = val.strip()
    else:
        addr = var.strip('me[]')
        num = bin(int(val))[2:].rjust(36, '0')
        bn = ''.join(num[i] if mask[i] == 'X' else mask[i] for i in range(36))
        mem[addr] = int(bn, 2)
print(sum(mem.values()))
mem.clear()
for line in lines:
    var, val = line.split(' = ')
    if var == 'mask':
        mask = val.strip()
    else:
        addr = int(var.strip('me[]'))
        num = bin(addr)[2:].rjust(36, '0')
        bn = ''.join(mask[i] if mask[i] != '0' else num[i] for i in range(36))
        for ad in rec(bn):
            mem[int(ad, 2)] = int(val)
print(sum(mem.values()))
