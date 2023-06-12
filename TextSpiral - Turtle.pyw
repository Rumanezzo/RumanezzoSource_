from turtle import bgcolor, speed, setup, textinput, title, color, down, ht, up, fd, write, lt, goto, clear, exitonclick

bgcolor('black')
speed(0)
setup(0.99, 0.9, 0, 0)
colors = ['red', 'yellow', 'blue', 'green']
title('Спираль из введённого текста')
ht()

name = textinput('Введите своё имя', 'Как тебя зовут?') or "Обормот"
for x in range(264):
    color(colors[x % 4])
    up()
    fd(x * 4)
    down()
    write(name, font=('FreeMono', int((x + 4) / 4), 'bold'))
    lt(92)

goto(0, 0)
color('red')
clear()
write(name, font=('Special Elite', 120, 'normal'), align='center')
title('Программа закончила свою работу!')

exitonclick()
