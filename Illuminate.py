from turtle import fd, rt, goto, tracer, bgcolor, pensize, Screen
from turtle import done, begin_fill, end_fill, fillcolor
import colorsys

s = Screen()
s.setup(0.99, 0.9, 0, 0)
tracer(100)
bgcolor("black")
h = 0.7
pensize(4)


def a():
    global h
    for _ in range(4):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        fillcolor(c)
        h += 0.004
        begin_fill()
        fd(50)
        rt(20)
        fd(40)
        rt(9)
        end_fill()


for i in range(400):
    a()
    goto(0, 0)
    rt(1)
done()
