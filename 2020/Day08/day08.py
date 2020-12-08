def rec(i=0, acc=0, use=False):
    if i >= n:
        return acc
    if vlines[i][1]:
        return None
    vlines[i][1] = True
    opr, arg = vlines[i][0].split()
    if opr == 'acc':
        res = rec(i + 1, acc + int(arg), use)
    elif opr == 'nop':
        res = rec(i + 1, acc, use) or (rec(i + int(arg), acc, True) if not use else None)
    else:
        res = rec(i + int(arg), acc, use) or (rec(i + 1, acc, True) if not use else None)
    vlines[i][1] = False
    return res


lines = open('inp08').readlines()
n = len(lines)
vlines = [[line, False] for line in lines]
acc = i = 0
while lines[i]:
    opr, arg = lines[i].split()
    lines[i] = ''
    if opr == 'nop':
        i += 1
    elif opr == 'acc':
        acc += int(arg)
        i += 1
    else:
        i += int(arg)

print(acc, rec(), sep='\n')
