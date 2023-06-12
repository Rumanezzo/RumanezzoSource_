from turtle import setup, shape, width, speed, bgcolor, numinput, color, exitonclick, fd, rt

setup(0.99, 0.9, 0, 0)
bgcolor('black')  # Цвет Фона
shape('turtle')  # Форма Черепашки
width(5)  # Ширина Линии
speed(0)  # Скорость Движения
color('white', 'black')

# Начало Программы

length0 = numinput('Длина Шага', 'Введите [3..10]', 5)
angle0 = numinput('Угол Поворота', 'Введите [10..175]', 60)
increment0 = numinput('Прирост Линии', 'Введите [1..5]', 3)
times0 = numinput('Сколько Линий', 'Введите [5..200]', 40)


def spiral(length, angle, increment, times):
    fd(length)
    rt(angle)
    if times == 0:
        return
    spiral(length + increment, angle, increment, times - 1)


spiral(length0, angle0, increment0, times0)

# Конец Программы
exitonclick()
