nums = list(map(int, input().split(',')))
ans = min(sum(abs(n - i) for n in nums) for i in range(max(nums)))
print(ans)
ans2 = min(sum(abs(n - i) * (abs(n - i) + 1) // 2 for n in nums) for i in range(max(nums)))
print(ans2)