import sys

nums = list(map(int, sys.stdin.read().split()))
ans1 = ans2 = 0
for i in range(len(nums) - 1):
    ans1 += nums[i] < nums[i + 1]
    ans2 += i + 3 < len(nums) and nums[i] < nums[i + 3]

print(ans1)
print(ans2)
