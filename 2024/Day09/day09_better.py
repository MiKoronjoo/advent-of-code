disk = list(map(int, input()))
blocks1 = []
sizes = []
for i, c in enumerate(disk):
    if i % 2 == 0:
        blocks1.extend(c * [i // 2])
        sizes.append(c)
    else:
        blocks1.extend(c * [None])
blocks2 = blocks1.copy()
sj = 0
for i in range(len(blocks1) - 1, -1, -1):
    if blocks1[i] is not None:
        for j in range(sj, i):
            if blocks1[j] is None:
                blocks1[i], blocks1[j] = blocks1[j], blocks1[i]
                break
        else:
            break
        sj = j + 1
ans1 = sum(i * c for i, c in enumerate(blocks1) if c is not None)
print(ans1)

head = len(blocks2) - 1
for s in range(len(sizes) - 1, 0, -1):
    while blocks2[head] != s:
        head -= 1
    cur = 1
    ll = sizes[s]
    while cur < len(disk):
        if disk[cur] >= ll:
            tail = sum(disk[:cur])
            for _ in range(ll):
                blocks2[head], blocks2[tail] = blocks2[tail], blocks2[head]
                head -= 1
                tail += 1
            disk[cur - 1] += ll
            disk[cur] -= ll
            disk.pop()
            disk.pop()
            break
        else:
            cur += 2
    else:
        disk.pop()
        disk.pop()

ans2 = sum(i * c for i, c in enumerate(blocks2) if c is not None)
print(ans2)
