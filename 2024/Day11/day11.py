from collections import defaultdict

stones = defaultdict(int)
for s in map(int, input().split()):
    stones[s] += 1

for blink in range(75):
    copy = stones.copy()
    for s, n in stones.items():
        if s == 0:
            copy[1] += n
        elif len(str_s := str(s)) % 2 == 0:
            s0, s1 = int(str_s[:len(str_s) // 2]), int(str_s[len(str_s) // 2:])
            copy[s0] += n
            copy[s1] += n
        else:
            copy[s * 2024] += n
        copy[s] -= n
    stones = copy
    if blink == 24:
        print(sum(stones.values()))

print(sum(stones.values()))
