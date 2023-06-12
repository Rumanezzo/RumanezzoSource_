from turtle import Turtle, Screen

t1 = Turtle()
t2 = Turtle()

s = Screen()

s.setup(0.99, 0.9, 0, 0)
s.bgcolor(0.7, 0.7, 0.7)

w0 = s.window_width()
h0 = s.window_height()
s.title(f'Ширина - {w0}, Высота - {h0}')
s.mode('logo')

t1.shape('triangle')
t2.shape('circle')
t1.width(5)
t2.width(6)
t1.color(0.7, 0.3, 0.1)
t2.color(0.1, 0.7, 0.3)

t1.fd(100)
t1.stamp()
t2.bk(100)
t2.stamp()
t1.rt(45)
t1.fd(50)
t2.lt(45)
t2.fd(50)






s.exitonclick()