def rec(i):
    if mem[i]:
        return mem[i]
    if i == N - 1:
        return 1
    res = 0
    for j in range(i + 1, min(i + 4, N)):
        if nums[j] - nums[i] < 4:
            res += rec(j)
    mem[i] = res
    return res


nums = sorted(map(int, open('inp10').readlines()))
nums.append(nums[-1] + 3)
prv = j1 = j3 = 0
for n in nums:
    if n - prv == 1:
        j1 += 1
    elif n - prv == 3:
        j3 += 1
    prv = n
print(j1 * j3)
nums.insert(0, 0)
N = len(nums)
mem = [0] * N
print(rec(0))
