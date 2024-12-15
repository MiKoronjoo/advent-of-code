import sys


class Robot:
    def __init__(self, str_warehouse):
        self.warehouse = [list(row) for row in str_warehouse.split()]
        for x in range(len(self.warehouse)):
            for y in range(len(self.warehouse[0])):
                if self.warehouse[x][y] == '@':
                    self.x = x
                    self.y = y
                    return

    def print_warehouse(self):
        print('\n'.join(''.join(row) for row in self.warehouse))

    def gps_coordinates(self):
        return sum(100 * x + y for x in range(len(self.warehouse)) for y in range(len(self.warehouse[0]))
                   if self.warehouse[x][y] == 'O')

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
            return
        elif self.warehouse[x][y] == '#':
            return
        else:  # 'O'
            nx, ny = x, y
            while True:
                x += dx
                y += dy
                if self.warehouse[x][y] == '.':
                    self.warehouse[x][y] = 'O'
                    self.warehouse[nx][ny] = '@'
                    self.warehouse[self.x][self.y] = '.'
                    self.x, self.y = nx, ny
                    return
                elif self.warehouse[x][y] == '#':
                    return


str_warehouse, movements = sys.stdin.read().split('\n\n')
robot = Robot(str_warehouse)
for m in movements.replace('\n', ''):
    robot.move(m)

robot.print_warehouse()
print(robot.gps_coordinates())
