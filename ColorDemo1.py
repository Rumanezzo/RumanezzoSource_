import turtle as t
import colorsys as cs

t.setup(0.99, 0.9, 0, 0)
t.title('Секторами рисуем...')
t.ht()

t.speed('fastest')
t.width(2)
t.bgcolor('black')
t.seth(45)

n = 360
n0 = 9

for i in range(n):
    t.begin_fill()
    t.color(cs.hsv_to_rgb(i/n0, i/n, 0.8))
    t.fillcolor(cs.hsv_to_rgb(i/n0, i/n, 1))
    t.rt(90)
    t.circle(i*1.2, 90)
    t.end_fill()
    t.rt(360 // n0 - 1)
    t.title(f'Секторами рисуем - {i}-й цикл!')

t.done()
