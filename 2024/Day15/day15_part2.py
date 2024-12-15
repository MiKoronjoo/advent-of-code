import sys


class Robot:
    def __init__(self, str_warehouse):
        self.warehouse = []
        for row in str_warehouse.split():  # type: str
            line = list(row.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'))
            self.warehouse.append(line)
        self.cache = {}
        for x in range(len(self.warehouse)):
            for y in range(len(self.warehouse[0])):
                if self.warehouse[x][y] == '@':
                    self.x, self.y = x, y
                    return

    def print_warehouse(self):
        print('\n'.join(''.join(row) for row in self.warehouse))

    def gps_coordinates(self):
        return sum(100 * x + y for x in range(len(self.warehouse)) for y in range(len(self.warehouse[0]))
                   if self.warehouse[x][y] == '[')

    def helper(self, x, y, movement, sec=False):
        if self.warehouse[x][y] == '.':
            return set()
        if self.warehouse[x][y] == '#':
            return None
        if (x, y) in self.cache:
            return self.cache[x, y]
        dx = -1 if movement == '^' else 1
        dy = -1 if self.warehouse[x][y] == ']' else 1
        res = None
        if (xs := self.helper(x + dx, y, movement)) is not None:
            if not sec:
                if (ys := self.helper(x, y + dy, movement, sec=True)) is not None:
                    res = {(x, y)} | xs | ys
            else:
                res = {(x, y)} | xs
        self.cache[x, y] = res
        return res

    def move(self, movement):
        if movement == '<':
            dx, dy = 0, -1
        elif movement == '>':
            dx, dy = 0, 1
        elif movement == '^':
            dx, dy = -1, 0
        else:  # 'v'
            dx, dy = 1, 0
        x, y = self.x + dx, self.y + dy
        if self.warehouse[x][y] == '.':
            self.warehouse[x][y] = '@'
            self.warehouse[self.x][self.y] = '.'
            self.x, self.y = x, y
        elif self.warehouse[x][y] == '#':
            return
        elif movement in '<>':  # '[]'
            while True:
                x += dx
                y += dy
                if self.warehouse[x][y] == '.':
                    self.warehouse[x].pop(y)
                    self.warehouse[x].insert(self.y, '.')
                    self.y += dy
                    return
                elif self.warehouse[x][y] == '#':
                    return
        else:  # '^v' '[]'
            self.cache.clear()
            if not (points := self.helper(x, y, movement)):
                return
            for px, py in sorted(points, reverse=(movement != '^')):
                self.warehouse[px][py], self.warehouse[px + dx][py] = \
                    self.warehouse[px + dx][py], self.warehouse[px][py]
            self.warehouse[self.x][self.y] = '.'
            self.x += dx
            self.warehouse[self.x][self.y] = '@'


str_warehouse, movements = sys.stdin.read().split('\n\n')
robot = Robot(str_warehouse)
for m in movements.replace('\n', ''):
    robot.move(m)

robot.print_warehouse()
print(robot.gps_coordinates())
