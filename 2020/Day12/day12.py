class Ship:
    def __init__(self):
        self.face = 0
        self.x = self.y = 0
        self.d = {0: self.e, 90: self.n, 180: self.e, 270: self.n}

    def f(self, num):
        self.d[self.face](num if self.face in (0, 270) else -num)

    def r(self, deg):
        self.face += deg
        self.face %= 360

    def n(self, num):
        self.y += num

    def e(self, num):
        self.x += num


class Ship2:
    def __init__(self):
        self.wp = [10, 1]
        self.x = self.y = 0

    def f(self, num):
        self.x += self.wp[0] * num
        self.y += self.wp[1] * num

    def r(self, deg):
        for _ in range(deg % 360 // 90):
            self.wp[0], self.wp[1] = self.wp[1], -self.wp[0]

    def n(self, num):
        self.wp[1] += num

    def e(self, num):
        self.wp[0] += num


def run(ship, cmds):
    for cmd in cmds:
        c = cmd[0].lower()
        num = int(cmd[1:])
        ship.__getattribute__(c)(num)
    return abs(ship.x) + abs(ship.y)


cmds = open('inp12').read().replace('L', 'R-').replace('S', 'N-').replace('W', 'E-').split()
print(run(Ship(), cmds), run(Ship2(), cmds), sep='\n')
