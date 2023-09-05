from turtle import Screen, Turtle
from math import sin, cos

magic = 20


def f1(time): return cos(time) * time * magic


def f2(time): return sin(time) * time * magic


s0 = Screen()
s0.bgcolor('grey')
s0.setup(0.99, 0.9, 0, 0)
s0.title('Рисуем sin и cos!')


t1 = Turtle()
t2 = Turtle()

t1.ht()
t2.ht()

t1.color('green')
t2.color('orange')

t1.width(4)
t2.width(3)

t1.pu()
t2.pu()

x0 = 400
time0 = -magic

y0 = f1(time0)
y1 = f2(time0)

t1.goto(-x0, y0)
t2.goto(-x0, y1)

t1.pd()
t2.pd()

for x in range(-x0, x0):
    y0 = f1(time0)
    y1 = f2(time0)
    time0 += 0.05
    t1.goto(x, y0)
    t2.goto(x, y1)

s0.exitonclick()
