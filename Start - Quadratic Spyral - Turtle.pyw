from turtle import color, setup, title, shape, bgcolor, width, speed
from turtle import home, numinput, exitonclick, ht, lt, rt, fd, pu, pd

colors = ("red", "blue", "green", "yellow", "orange", "purple", "pink", "violet", "aquamarine",
          "bisque", "burlywood", "chartreuse", "magenta", "moccasin", "navy", "plum", "tan",
          "turquoise", "tomato", "brown", "salmon", "gold", "cornsilk", "maroon", "sienna",
          "crimson", "greenyellow", "crimson")

setup(0.99, 0.9, 0, 0)
title('Квадратные спирали - много цветов, разная толщина')
shape('turtle')
color('white')
bgcolor('black')
width(0)
speed(0)
ht()


def spiral():
    for i, name in enumerate(colors):
        color(name)
        fd(120 + 10 * i)
        lt(90)
        width(i % 5)
    pu()
    home()
    pd()


def result(x):
    n = int(x)
    for i in range(n):
        spiral()
        rt(360 / n * (1 + i))

x0 = numinput('Сколько спиралей?', 'Минимальное-3, Максимальное-21', 5, 3, 21)
result(x0)
exitonclick()
