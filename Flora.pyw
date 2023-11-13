import turtle as t
import colorsys as cs

s0 = t.Screen()
s0.setup(0.99, 0.9, 0, 0)
t.speed(0)
t.tracer(20)
t.width(1)
t.bgcolor('black')
t.ht()
s0.title('Цветочек - с лепесточками')
for ii in range(25):
    for i in range(15):
        t.color(cs.hsv_to_rgb(i/15, ii/25, 1))
        t.rt(90)
        t.circle(200-ii*4, 90)
        t.lt(90)
        t.circle(200-ii*4, 90)
        t.rt(180)
        t.circle(50, 24)

s0.title('Работа завершена!')
s0.exitonclick()       
    