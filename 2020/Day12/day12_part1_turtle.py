from turtle import Turtle, Screen

ship = Turtle()
wn = Screen()
wn.tracer(0)
for cmd in open('inp12').readlines():
    c, num = cmd[0], int(cmd[1:])
    if c == 'N':
        ship.sety(ship.ycor() + num)
    elif c == 'S':
        ship.sety(ship.ycor() - num)
    elif c == 'E':
        ship.setx(ship.xcor() + num)
    elif c == 'W':
        ship.setx(ship.xcor() - num)
    elif c == 'L':
        ship.left(num)
    elif c == 'R':
        ship.right(num)
    else:
        ship.forward(num)
print(int(abs(ship.xcor()) + abs(ship.ycor())))
wn.exitonclick()
