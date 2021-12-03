import sys

nums = sys.stdin.read().split()
gma = ''
eps = ''
for i in range(len(nums[0])):
    if sum(n[i] == '1' for n in nums) > len(nums) / 2:
        gma += '1'
        eps += '0'
    else:
        gma += '0'
        eps += '1'

print(int(gma, 2) * int(eps, 2))

oxy = nums.copy()
i = 0
while len(oxy) != 1:
    most = '1' if sum(n[i] == '1' for n in oxy) >= len(oxy) / 2 else '0'
    oxy = [n for n in oxy if n[i] == most]
    i += 1

co2 = nums
i = 0
while len(co2) != 1:
    least = '1' if sum(n[i] == '1' for n in co2) < len(co2) / 2 else '0'
    co2 = [n for n in co2 if n[i] == least]
    i += 1

print(int(oxy[0], 2) * int(co2[0], 2))
