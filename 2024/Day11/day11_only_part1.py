def change(num: int):
    if num == 0:
        return 1,
    elif len(snum := str(num)) % 2 == 0:
        return int(snum[:len(snum) // 2]), int(snum[len(snum) // 2:])
    return num * 2024,


stones = list(map(int, input().split()))

for _ in range(25):
    new_stones = []
    for s in stones:
        new_stones.extend(change(s))
    stones = new_stones

print(len(stones))
