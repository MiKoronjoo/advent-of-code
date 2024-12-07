import sys
import copy


class Guard:
    def __init__(self, i, j, mapped_area):
        self.s_i = i
        self.s_j = j
        self.i = i
        self.j = j
        self.faces = ['up', 'right', 'down', 'left']
        self.map = copy.deepcopy(mapped_area)

    def reset(self):
        self.i = self.s_i
        self.j = self.s_j
        self.faces = ['up', 'right', 'down', 'left']

    @property
    def face(self):
        return self.faces[0]

    def rotate(self):
        self.faces.append(self.faces.pop(0))

    def next(self):
        if self.face == 'up':
            return self.i - 1, self.j
        elif self.face == 'right':
            return self.i, self.j + 1
        elif self.face == 'down':
            return self.i + 1, self.j
        else:  # left
            return self.i, self.j - 1

    def run(self, result=True):
        xs = set()
        temp = set()
        while True:
            if (current := (self.i, self.j, self.face)) not in temp:
                temp.add(current)
            else:
                return
            i, j = self.next()
            if 0 <= i < len(self.map) and 0 <= j < len(self.map[0]):
                if self.map[i][j] == '#':
                    self.rotate()
                else:
                    if result:
                        xs.add((self.i, self.j))
                    self.i = i
                    self.j = j
            else:
                if result:
                    xs.add((self.i, self.j))
                break
        return xs

    def loop(self, xs):
        ans = 0
        for i, j in xs:
            self.map[i][j] = '#'
            self.reset()
            ans += self.run() is None
            self.map[i][j] = '.'
        return ans


area = [list(row) for row in sys.stdin.read().split()]
for _i in range(len(area)):
    for _j in range(len(area[0])):
        if area[_i][_j] == '^':
            break
    else:
        continue
    break

guard = Guard(_i, _j, area)
xs = guard.run()
print(len(xs))
print(guard.loop(xs))
