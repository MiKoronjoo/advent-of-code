class Ship:
    def __init__(self):
        self.face = 0
        self.x = self.y = 0
        self.d = {0: self.e, 90: self.s, 180: self.w, 270: self.n}

    def fd(self, num):
        self.d[self.face](num)

    def lt(self, deg):
        self.face -= deg
        self.face %= 360

    def rt(self, deg):
        self.face += deg
        self.face %= 360

    def n(self, num):
        self.y += num

    def s(self, num):
        self.y -= num

    def e(self, num):
        self.x += num

    def w(self, num):
        self.x -= num

    def man_dis(self):
        return abs(self.x) + abs(self.y)


class Ship2:
    def __init__(self):
        self.wp = [10, 1]
        self.x = self.y = 0

    def fd(self, num):
        self.x += self.wp[0] * num
        self.y += self.wp[1] * num

    def lt(self, deg):
        self.rt(-deg % 360)

    def rt(self, deg):
        for _ in range(deg // 90):
            self.wp[0], self.wp[1] = self.wp[1], -self.wp[0]

    def n(self, num):
        self.wp[1] += num

    def s(self, num):
        self.wp[1] -= num

    def e(self, num):
        self.wp[0] += num

    def w(self, num):
        self.wp[0] -= num

    def man_dis(self):
        return abs(self.x) + abs(self.y)


ship = Ship()
ship2 = Ship2()
for cmd in open('inp12').readlines():
    c = cmd[0]
    num = int(cmd[1:])
    if c == 'N':
        ship.n(num)
        ship2.n(num)
    elif c == 'S':
        ship.s(num)
        ship2.s(num)
    elif c == 'E':
        ship.e(num)
        ship2.e(num)
    elif c == 'W':
        ship.w(num)
        ship2.w(num)
    elif c == 'L':
        ship.lt(num)
        ship2.lt(num)
    elif c == 'R':
        ship.rt(num)
        ship2.rt(num)
    else:
        ship.fd(num)
        ship2.fd(num)
print(ship.man_dis())
print(ship2.man_dis())
