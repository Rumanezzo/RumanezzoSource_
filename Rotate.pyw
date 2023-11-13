from turtle import fd, rt, lt, ht, circle, speed, bgcolor, width, tracer, color, exitonclick
from turtle import Screen
from colorsys import hsv_to_rgb

speed(0)
ht()
tracer(5)
bgcolor('black')
s0 = Screen()

s0.setup(0.99, 0.9, 0, 0)
width(2)
n = 180
h0 = 0.01
r0 = 90
l0 = 135

angle = 180 / n


def figure(h, flag=1, r=r0, length=l0):
    color(hsv_to_rgb(h, 1, 1))
    fd(length)
    rt(60 * flag)
    fd(length)
    lt(120 * flag)
    circle(r * flag)
    rt(240 * flag)
    fd(length)
    rt(60 * flag)
    fd(length)
    h += 0.02
    return h


for i in range(n):
    h0 = figure(h0, r=-r0 + i // 500 * r0, length=l0 + i // 500 * l0)
    h0 = figure(h0, r=-r0 + i // 500 * r0, length=l0 + i // 500 * l0, flag=-1)
    lt(angle)
    s0.title(f'{n - i - 1}')

s0.title('Работа выполнена - кликнете по окну!')
exitonclick()
