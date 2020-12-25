def loop(goal, sn=7):
    i = 0
    n = 1
    while n != goal:
        i += 1
        n *= sn
        n %= 20201227
    return i


def loop2(sn, ls):
    n = 1
    for _ in range(ls):
        n *= sn
        n %= 20201227
    return n


card_pk = int(input())
door_pk = int(input())
cls = loop(card_pk)
dls = loop(door_pk)
print(loop2(door_pk, cls))
print(loop2(card_pk, dls))
