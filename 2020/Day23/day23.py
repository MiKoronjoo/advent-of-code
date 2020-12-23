class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, size, iterable=None):
        self.front = None
        self.back = None
        self.nodes = [None] * (size + 1)
        if iterable is not None:
            for val in iterable:
                self.append(val)

    def append(self, val):
        node = Node(val)
        self.nodes[val] = node
        if self.front is None:
            self.front = node
        else:
            self.back.next = node
        self.back = node
        self.back.next = self.front

    def appendleft(self, val):
        node = Node(val)
        self.nodes[val] = node
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            node.next = self.front
            self.front = node

    def rotateleft(self):
        self.back = self.front
        self.front = self.front.next

    def popleft(self):
        res = self.front
        self.back.next = self.front.next
        self.front = self.back.next
        res.next = None
        return res

    def special_insert(self, val, lst):
        node = self.nodes[val]
        flag = node == self.back
        tmp = node.next
        for n in lst:
            node.next = n
            node = n
        node.next = tmp
        if flag:
            self.back = node


def calc(dq, size, moves):
    for _ in range(moves):
        dest = dq.front.val
        dq.rotateleft()
        pickup = [dq.popleft() for _ in range(3)]
        while dest > 1:
            dest -= 1
            if dq.nodes[dest] not in pickup:
                break
        else:
            dest = next(x for x in range(size, size - 5, -1) if dq.nodes[x] not in pickup)
        dq.special_insert(dest, pickup)
    return dq.nodes[1]


inp = list(map(int, input()))
cups = LinkedList(len(inp), inp)
node = calc(cups, len(inp), 100)
tmp = node.next
ans = ''
while tmp != node:
    ans += str(tmp.val)
    tmp = tmp.next
print(ans)

SIZE = 1000000
dq = LinkedList(SIZE, inp)
for n in range(10, SIZE + 1):
    dq.append(n)
nd = calc(dq, SIZE, SIZE * 10)
print(nd.next.val * nd.next.next.val)
