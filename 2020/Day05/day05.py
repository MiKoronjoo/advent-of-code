def bs(code: str, start: int, end: int) -> int:
    if not code:
        return start
    if code[0] in 'LF':
        return bs(code[1:], start, end - (end - start + 1) // 2)
    return bs(code[1:], start + (end - start + 1) // 2, end)


def get_seat_id(code: str) -> int:
    row = bs(code[:7], 0, 127)
    column = bs(code[7:], 0, 7)
    return row * 8 + column


if __name__ == '__main__':
    lst = sorted(get_seat_id(code) for code in open('inp05').read().split())
    print(lst[-1])
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] != 1:
            print(lst[i] - 1)
            break
