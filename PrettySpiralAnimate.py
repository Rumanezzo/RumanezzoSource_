import turtle

colors = ('red', 'purple', 'blue', 'green', 'yellow', 'orange')
t = turtle.Pen()

screen = turtle.Screen()
screen.mode('logo')
screen.setup(0.99, 0.9, 0, 0)

screen.tracer(0)
turtle.speed(0)
turtle.delay(0)

turtle.bgcolor('black')
t.ht()


def pattern(step):
    for i in range(360):
        t.pencolor(colors[i % 6])
        t.width(x // 100 + 1)
        t.fd(i * step)
        t.rt(59)


step0 = 0.5
v = 0.04

for x in range(600):
    screen.title(f'{x}-й цикл')
    t.clear()
    pattern(step0)
    screen.update()
    t.home()
    t.rt(x)
    step0 += v
    if step0 > 5 or step0 < 0.1:
        v = -v

screen.exitonclick()
