import sys


def dog(n1: int, n2: int) -> int:
    nn = str(n1)[:-len(str(n2))]
    return int(nn) if nn else 0


def possible(value: int, nums: list, concat: bool) -> bool:
    if value == 0 and not nums:
        return True
    if value < 0 or not nums:
        return False
    if value % nums[-1] == 0 and possible(value // nums[-1], nums[:-1], concat):
        return True
    if concat and str(value).endswith(str(nums[-1])) and possible(dog(value, nums[-1]), nums[:-1], concat):
        return True
    return possible(value - nums[-1], nums[:-1], concat)


ans1 = ans2 = 0
for line in sys.stdin.readlines():
    tv, ns = line.split(':')
    test_value, numbers = int(tv), list(map(int, ns.split()))
    ans1 += possible(test_value, numbers, concat=False) and test_value
    ans2 += possible(test_value, numbers, concat=True) and test_value
print(ans1)
print(ans2)
