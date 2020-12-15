lst = list(map(int, input().split(',')))
mem = {x: i for i, x in enumerate(lst[:-1])}
size = len(lst)
last = lst[-1]
while size != 30000000:
    if size == 2020:
        print(last)
    i = mem.get(last, size - 1)
    mem[last] = size - 1
    last = size - 1 - i
    size += 1
print(last)
