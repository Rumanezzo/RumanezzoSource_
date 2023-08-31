from turtle import *
from random import randint
from keyboard import read_event, KEY_DOWN

symbols_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789."
symbols_eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = symbols_rus + symbols_eng

colors = {5: 'lightgreen', 4: 'green', 3: 'orange', 2: 'red'}
results = {5: 'Отлично!', 4: 'Хорошо!', 3: 'Так себе!', 2: 'Отвратительно!'}
mistakes = 0

s0 = Screen()
s0.title('Пробуем имитацию консоли черепашкой... - тренажер умножения')
s0.setup(0.99, 0.9, -1, 0)
s0.mode('logo')

color_back = 'AntiqueWhite'
colorfont = 'Black'
colorfont0 = 'Blue'
s0.bgcolor(color_back)

font_size = 32
font = ('Special Elite', font_size, 'bold')

x0 = - s0.window_width() // 2 + font_size + 20
y0 = s0.window_height() // 2 - font_size - 20

t0 = Turtle()
t0.speed(0)
t0.shape('triangle')


def key_pressed():
    str_out = ''
    while True:
        while True:
            event = read_event()
            if event.event_type == KEY_DOWN:
                key = event.name
                if key in symbols or key == 'enter' or key == 'backspace':
                    break

        if key == '.' or key == 'enter':
            break
        elif key == 'backspace':
            t0.color(color_back)
            t0.write(str_out, font=font)
            str_out = str_out[:-1]
            t0.color(colorfont)
            t0.write(str_out, font=font)
        else:
            str_out += key
            t0.write(str_out, font=font)

    return str_out


def text(n_str, txt='Здесь могла бы быть Ваша реклама...'):
    t0.pu()
    t0.goto(x0, y0 - n_str * (font_size + 10))
    t0.write(txt, font=font, move=True)


text(0, 'Давай проверим твою таблицу умножения...')
text(1, 'Кстати, как тебя зовут? ⟶ ')

name = key_pressed()

t0.color(color_back)
t0.write(name, font=font)
t0.color(colorfont0)
t0.write(f'Очень приятно, {name}!', font=font)
t0.color(colorfont)
text(2, 'Я составлю для тебя несколько примеров,')
text(3, 'а ты попробуешь с ними справиться...')
i = 0
for i in range(5, 10):
    f1 = randint(2, 9)
    f2 = randint(2, 9)
    text(i, f'{f1} × {f2} = ')
    ans = key_pressed()

    if int(ans) == f1 * f2:
        t0.color('green')
    else:
        t0.color('maroon')
        mistakes += 1
    t0.write(f'{ans}', font=font)
    t0.color('black')
else:
    last = i

success = 5 - mistakes
success = 2 if success < 2 else success

text(last + 2, f'{name}! Эта нелегкая работа была выполнена тобой...')
t0.color(colors[success])
text(last + 3, f'{results[success]}'*6)
s0.title('Для завершения программы - кликнете по окну!')
s0.exitonclick()
