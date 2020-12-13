ts = int(input())
buses = [(int(bus), -i % int(bus)) for i, bus in enumerate(input().split(',')) if bus != 'x']
# Part 1
a = 0
while True:
    for x, _ in buses:
        if (ts + a) % x == 0:
            print(a * x)
            break
    else:
        a += 1
        continue
    break
# Part 2: With help of https://dev.to/qviper/advent-of-code-2020-python-solution-day-13-24k4
r, ans = buses[0]
for bus, i in buses[1:]:
    while ans % bus != i:
        ans += r
    r *= bus
print(ans)
