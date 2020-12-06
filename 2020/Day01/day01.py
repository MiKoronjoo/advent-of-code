def calc(num=2020, start=0):
    j = n - 1
    for i in range(start, n):
        goal = num - ll[i]
        while i < j:
            if ll[j] == goal:
                return goal * ll[i]
            elif ll[j] < goal:
                break
            j -= 1
        else:
            return


ll = sorted(map(int, open('inp01').read().split()))
n = len(ll)
print(calc(2020))
for i in range(n):
    res = calc(2020 - ll[i], i + 1)
    if res is not None:
        print(res * ll[i])
        break
