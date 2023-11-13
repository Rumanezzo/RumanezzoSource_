from turtle import *
t = Turtle()
s = Screen()
shapes = ('arrow', 'turtle', 'circle', 'square', 'triangle', 'classic')
s.title('Черепашьи Формы...')
t.ht()
t.pu()
t.fd(-s.canvwidth * 0.99)

for i, shp in enumerate(shapes):    
    t.fd(100)
    t.circle(50 + 0.5 * i, 0.7)
    t.shape(shp)
    t.stamp()

s.exitonclick()
