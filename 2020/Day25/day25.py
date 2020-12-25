card_pk = int(input())
door_pk = int(input())
i = 0
n = 1
while n != door_pk:
    i += 1
    n *= 7
    n %= 20201227
print(pow(card_pk, i, 20201227))
