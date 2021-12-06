from collections import deque

lfs = list(map(int, input().split(',')))
DAYS1 = 80
DAYS2 = 256
state = deque(0 for _ in range(9))
for lf in lfs:
    state[lf] += 1

for _ in range(DAYS1):
    state.rotate(-1)
    state[6] += state[-1]
print(sum(state))

for _ in range(DAYS1, DAYS2):
    state.rotate(-1)
    state[6] += state[-1]
print(sum(state))
