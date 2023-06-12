from TurtleSetup import t0, s0

t0.width(6)
t0.speed(0)


s0.title(f'Размер окна -> ширина: {s0.window_width()} пкс., высота: {s0.window_height()} пкс.')

def thing(n, length, turn=t0.rt, width=8):
    alpha = 360 // n
    beta = (180 - alpha) // 2
    t0.width(width)
    
    for _ in range(n):
        t0.fd(length)    
        t0.dot(15)
    
        turn(alpha + beta)
        t0.fd(length // 4)
    
        t0.circle(20)
        t0.bk(length // 2)
        # t0.write(f'{_ + 1}', font=('FreeMono', 20, 'bold'))
        turn(-beta)

def multi_thing(n, length=250, n_turns=9):
    
    for _ in range(n_turns):
        t0.color('green')    
        thing(n, length, t0.rt, 6)
        t0.color('red')
        thing(n, length, t0.lt, 2)
        t0.rt(360 // n_turns)


multi_thing(3, 350, 10)
t0.goto(500, 0)
multi_thing(3, 150, 5)
t0.goto(-500, 0)
multi_thing(3, 150, 5)

s0.title('Я закончила! Нажми на экран!!!')
s0.exitonclick()