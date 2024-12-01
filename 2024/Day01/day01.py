import sys
nums = list(map(int, sys.stdin.read().split()))
ll = sorted(nums[0::2])
rl = sorted(nums[1::2])
print(sum(abs(ll[i] - rl[i]) for i in range(len(ll))))
print(sum(n * rl.count(n) for n in ll))
