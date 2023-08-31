from TurtleSetup import t0, s0, colors

font = ('FreeMono', 18, 'bold')
font0 = ('Special Elite', 33, 'bold')
t0.width(8)
t0.speed(0)
left_up_x = -s0.window_width() // 2 + 15
left_up_y = s0.window_height() // 2 - 20

t0.pu()
t0.goto(left_up_x, left_up_y)
t0.rt(90)

t0.st()
t0.pd()
t0.speed(0)
for _ in 2 *  colors:
    t0.color(_)
    t0.write(_, font=font)
    t0.fd(30)
    t0.rt(90)
    t0.fd(15)
    t0.lt(90)

t0.write('Демонстрация цветов...', font=font)
t0.ht()
t0.pu()
t0.goto(2 * left_up_x // 3, left_up_y - 20)
t0.color('maroon')
t0.write('Вот такие цвета я могу выводить на экран...', font=font0)
s0.title('Я закончила! Кликни по экрану!')
s0.exitonclick()