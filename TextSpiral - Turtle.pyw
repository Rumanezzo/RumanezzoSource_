from turtle import speed, color, down, ht, up, fd, lt, home
from turtle import clear, exitonclick, bgcolor, title, write, setup, textinput 
from time import sleep

bgcolor('black')
speed(0)
setup(0.99, 0.9, 0, 0)
colors = ['red', 'orange', 'blue', 'green']
title('Спиралькой имя твоя я закручу...')
ht()

name = textinput('Введи своё имя!', 'Как тебя зовут?') or "Обормот"
title(f'Кручу спираль из имени ⟶ {name}')
for x in range(264):
    color(colors[x % 4])
    up()
    fd(x * 4)
    down()
    write(name, font=('Special Elite', int((x + 4) / 4), 'bold'))
    lt(92)
sleep(2)

home()
clear()

color('red')
write('Теперь я знаю кто ты...', font=('Special Elite', 75, 'normal'), align='center')

sleep(2)
clear()

for _ in range(6):
    color('green')
    write(f'Ты - {name}!', font=('Special Elite', 120, 'normal'), align='center')
    sleep(1)
    color('red')
    write(f'Ты - {name}!', font=('Special Elite', 120, 'normal'), align='center')
    title(f'{6-_}')

title('Программа закончила свою работу ⟶ кликни на экран!')

exitonclick()
