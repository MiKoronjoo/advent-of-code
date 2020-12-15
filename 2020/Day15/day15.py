lst = list(map(int, input().split(',')))
mem = {x: i for i, x in enumerate(lst[:-1])}
while len(lst) != 30000000:
    last = lst[-1]
    i = mem.get(last)
    mem[last] = len(lst) - 1
    if i is None:
        lst.append(0)
    else:
        lst.append(len(lst) - 1 - i)
print(lst[2019], lst[-1], sep='\n')
