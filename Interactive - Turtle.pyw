from turtle import *

title('Интерактивная Черепашка - управляется с клавиатуры!')  # Заголовок
mode('logo')  # Черепашка на север
bgcolor('black')  # Цвет Фона
color('green', 'blue')  # Цвет Линии и Заливки
shape('turtle')  # Форма Черепашки
width(5)  # Ширина Линии
speed(0)  # Скорость Движения
s = Screen()
s.setup(0.99, 0.9, 0, 0)


def upper():
    fd(75)
    circle(50)


def downer():
    bk(50)
    circle(25)


def lefter():
    lt(30)
    fd(25)
    fd(-25)


def righter():
    rt(30)
    fd(25)
    fd(-25)


onkey(upper, "Up")
onkey(lefter, 'Left')
onkey(righter, 'Right')
onkey(downer, 'Down')

listen()
exitonclick()
