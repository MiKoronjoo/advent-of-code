class Ship:
    def __init__(self):
        self.face = 0
        self.x = self.y = 0
        self.d = {0: self.e, 90: self.n, 180: self.e, 270: self.n}

    def fd(self, num):
        self.d[self.face](num if self.face in (0, 270) else -num)

    def rt(self, deg):
        self.face += deg
        self.face %= 360

    def n(self, num):
        self.y += num

    def e(self, num):
        self.x += num

    def man_dis(self):
        return abs(self.x) + abs(self.y)


class Ship2:
    def __init__(self):
        self.wp = [10, 1]
        self.x = self.y = 0

    def fd(self, num):
        self.x += self.wp[0] * num
        self.y += self.wp[1] * num

    def rt(self, deg):
        deg %= 360
        for _ in range(deg // 90):
            self.wp[0], self.wp[1] = self.wp[1], -self.wp[0]

    def n(self, num):
        self.wp[1] += num

    def e(self, num):
        self.wp[0] += num

    def man_dis(self):
        return abs(self.x) + abs(self.y)


def run(ship, cmds):
    for cmd in cmds:
        c = cmd[0]
        num = int(cmd[1:])
        if c == 'N':
            ship.n(num)
        elif c == 'S':
            ship.n(-num)
        elif c == 'E':
            ship.e(num)
        elif c == 'W':
            ship.e(-num)
        elif c == 'R':
            ship.rt(num)
        elif c == 'L':
            ship.rt(-num)
        else:
            ship.fd(num)
    return ship.man_dis()


cmds = open('inp12').readlines()
print(run(Ship(), cmds))
print(run(Ship2(), cmds))
