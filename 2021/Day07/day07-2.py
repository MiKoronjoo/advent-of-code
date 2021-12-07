from statistics import median, mean

nums = list(map(int, input().split(',')))
med = int(median(nums))
print(sum(abs(med - n) for n in nums))
avg = round(mean(nums))
ans2 = min(sum(abs(n - i) * (abs(n - i) + 1) // 2 for n in nums) for i in (avg - 1, avg, avg + 1))
print(ans2)
