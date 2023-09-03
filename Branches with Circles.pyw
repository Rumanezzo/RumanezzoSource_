from turtle import Screen, Turtle
s0 = Screen()
s0.title('Рисуем узоры с кружочками...')
s0.setup(0.99, 0.9, 0, 0)
s0.mode('logo')
s0.bgcolor('orange')

t0 = Turtle()

font = ('Special Elite', 64, 'bold')

t0.width(1)
t0.speed(0)
t0.shape('arrow')
t0.ht()


def polygon(n=12, size=100, t=t0):
    t0.width(6)
    
    for _ in range(n):
        t.color("olive")
        t.fd(2 * size)
        t.color(0.8 - 0.01 * _, 0.6, 0.2 + 0.02 * _)
        t.dot(30)
        t.color("green")
        t.bk(size)
        t.rt(360 // n)

for i in range(5):
    polygon(18, 100 - 20 * i)
    t0.pu()
    t0.goto(50 + 50 * i, 0)
    t0.pd()

t0.color('lightgreen')
t0.speed(1)
t0.pu()
t0.goto(-s0.window_width() // 4, 0)
t0.color('green')
t0.write('Всё!!!', font=font)


s0.title('Работа выполнена! - кликнете на экран!')
s0.exitonclick()