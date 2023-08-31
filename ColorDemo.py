from turtle import ht, speed, bgcolor, width, color, circle, rt, done, setup
import colorsys

ht()
setup(0.99, 0.9,0, 0)
speed('fastest')
bgcolor('black')
width(2)
h = 0.0

for i in range(75):
    col = colorsys.hsv_to_rgb(h, 1, 1)
    color(col)
    for j in range(10):
        circle(i*2)
        rt(36)
    h += 0.1
done()
