import sys


def check(board):
    for row in board:
        if all(x == -1 for x in row):
            return True
    for j in range(len(board[0])):
        if all(x == -1 for x in (board[i][j] for i in range(len(board)))):
            return True
    return False


def score(board):
    return sum(x for row in board for x in row if x != -1)


fl, *rest = sys.stdin.read().strip().split('\n\n')
nums = list(map(int, fl.split(',')))
boards = [[list(map(int, x.strip().split())) for x in st.split('\n')] for st in rest]

res = []
for num in nums:
    for brd in boards:
        for i in range(len(brd)):
            for j in range(len(brd[0])):
                if brd[i][j] == num:
                    brd[i][j] = -1
    candidates = [brd for brd in boards if check(brd)]
    if candidates:
        winner = max(candidates, key=score)
        res.append(num * score(winner))
        for cand in candidates:
            boards.remove(cand)

print(res[0])
print(res[-1])
