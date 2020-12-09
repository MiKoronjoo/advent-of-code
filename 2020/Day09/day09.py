nums = list(map(int, open('inp09').readlines()))
prelen = 25
invalid = 0
for i, n in enumerate(nums[prelen:], prelen):
    for j in range(i - prelen, i):
        for k in range(i - prelen, i):
            if nums[j] + nums[k] == n:
                break
        else:
            continue
        break
    else:
        invalid = n
        break
print(invalid)
i = 0
j = 1
invalid -= nums[i] + nums[j]
while invalid:
    if invalid - nums[j+1] >= 0:
        invalid -= nums[j+1]
        j += 1
    else:
        invalid += nums[i]
        i += 1
rng = nums[i:j+1]
print(min(rng) + max(rng))
