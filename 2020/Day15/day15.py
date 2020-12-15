lst = list(map(int, input().split(',')))
mem = {x: i for i, x in enumerate(lst)}
while len(lst) != 30000000:
    if len(lst) == 2020:
        print(lst[-1])
    n = lst[-1]
    i = mem.get(n)
    mem[n] = len(lst) - 1
    if i is None:
        lst.append(0)
    else:
        lst.append(len(lst) - 1 - i)
print(lst[-1])
