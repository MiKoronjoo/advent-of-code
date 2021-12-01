import sys

nums = list(map(int, sys.stdin.read().split()))
ans1 = ans2 = 0
for i in range(len(nums) - 1):
    ans1 += nums[i] < nums[i + 1]
    ans2 += sum(nums[i:i + 3]) < sum(nums[i + 1:i + 4])

print(ans1)
print(ans2)
