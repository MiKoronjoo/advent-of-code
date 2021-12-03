import sys

nums = sys.stdin.read().split()
gma = 0
eps = 0
for i in range(len(nums[0])):
    gma <<= 1
    eps <<= 1
    if sum(n[i] == '1' for n in nums) > len(nums) / 2:
        gma += 1
    else:
        eps += 1

print(gma * eps)

oxy = nums.copy()
i = 0
while len(oxy) != 1:
    ones = list(filter(lambda x: x[i] == '1', oxy))
    zeros = list(filter(lambda x: x[i] == '0', oxy))
    oxy = ones if len(ones) >= len(zeros) else zeros
    i += 1

co2 = nums
i = 0
while len(co2) != 1:
    ones = list(filter(lambda x: x[i] == '1', co2))
    zeros = list(filter(lambda x: x[i] == '0', co2))
    co2 = ones if len(ones) < len(zeros) else zeros
    i += 1

print(int(oxy[0], 2) * int(co2[0], 2))
