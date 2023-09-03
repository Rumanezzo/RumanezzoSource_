import turtle
clicks = 0

names = ('Tess', 'Alex', 'Mary', 'Mike', 'Yana', 'Mara', 'Crash', 'Rusha', 'Speck', 'Rusti', 'Gaia', 'Nick')
colors = ('green', 'orange', 'red', 'yellow', 'blue', 'violet', 'purple', 'cyan', 'magenta', 'lightgreen', 'lightblue')

def make_window(col='grey', title="Здесь гуляют Черепахи"):
    w = turtle.Screen()
    w.bgcolor(col)
    w.title(title)
    w.mode('logo')
    w.colormode(255)
    w.delay(10)
    
    wmax = w.window_width() // 2
    hmax = w.window_height() // 2
    
    return w, wmax, hmax


wn, wm, hm = make_window(title='Ловим Мышиные Клики!')
wn.setup(0.99, 0.9, 0, 0)

def make_turtle(name='Marina', col='red', wd=5, shp='turtle', sz=10, angle=0, length=100):
    t = turtle.Turtle()
    t.shape(shp)
    t.shapesize(sz)
    t.color(col)

    t.width(wd)
    t.rt(angle)
    t.fd(length)    
    
    return t, name


def make_coda():
    t = turtle.Turtle()
    t.ht()
    t.pu()
    t.goto(wm*0.99, hm*0.99)
    t.color('black')
    t.shape('circle')
    t.st()
    
    return t


def piruet(t, r=100):
    t.rt(90)
    t.circle(r)
    t.rt(90)
    t.pu()
    t.fd(-r)
    t.stamp()
    t.lt(15)
    t.pd()
    
    
def handler_coda(x, y):
    wn.title(f'Завершаем работу в точке ({x}, {y})! Кликнете на экран! {wm}, {hm}')
    wn.exitonclick()


def handler(x, y):
    global clicks
    clicks += 1
    wn.title(f'Задета по координатам ({x}, {y}), {clicks}-й клик!')
    for n, i in enumerate(turtles):
        piruet(i, 30+10*n)


#Первоначальные настройки
turtles = []

for _, name0 in enumerate(names):
    t0 = make_turtle(name=name0, sz=1+0.1*_, col=colors[_%10], wd=6+0.5*_, length=(0.9-0.05*_)*hm, angle=29*_)
    t0[0].onclick(handler)
    turtles.append(t0[0])
    
coda = make_coda()
#Конец первоначальных настроек
for _ in turtles:
    t0[0].onclick(handler)


coda.onclick(handler_coda)

wn.mainloop()
