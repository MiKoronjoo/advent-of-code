import sys

s = g = 0
for line in sys.stdin.readlines():
    report = list(map(int, line.split()))
    if report[-1] < report[0] and report[-1] < report[1]:
        report.reverse()
    s += all(0 < report[j] - report[j - 1] < 4 for j in range(1, len(report)))
    g += any(all(0 < r[j] - r[j - 1] < 4 for j in range(1, len(r))) for r
                in (report[:i] + report[i + 1:] for i in range(len(report))))

print(s)
print(g)
