from turtle import Turtle, Screen


# Turtle - class, Screen - function, returns class! Attention!!!


class Tortilla(Turtle):
    def __init__(self, color1='white', color2='green'):
        super().__init__()
        self.color(color1, color2)
        self.shape('triangle')
        self.width(3)
        self.speed(5)


# ----------------------------Инициализируем экран для работы-----------------------------
s0 = Screen()  # Вызов функции, возвращающей объект типа "Экран"...
font = ('FreeMono', 14, 'bold')
t0 = Tortilla()  # Создали "предустановленную" черепашку

s0.title('Черепашья Графика - предустановленные параметры')
s0.setup(0.99, 0.9, 0, 0)  # Пропорции относительно полного экрана и координаты левого
# верхнего угла
# Установка Размеров Окна на весь экран - пользуемся везде где можно!
s0.mode('logo')  # Черепашка на север - мордой вверх!

# Граничные точки
step = 20
xr = s0.window_width() // 2 - step  # Самая правая
xl = -xr  # Самая левая
yu = s0.window_height() // 2 - step  # Самая верхняя
yd = -yu  # Самая нижняя

s0.bgcolor('grey')
# -------------------------------Конец инициализации экрана-------------------------------

colors = (
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "violet", "aquamarine",
    "bisque", "burlywood", "chartreuse", "magenta", "moccasin", "navy", "plum", "tan",
    "thistle", "turquoise", "tomato", "brown", "salmon", "gold", "maroon", "sienna",
    "peru", "lightgreen", "cyan",)

n_colors = len(colors)

if __name__ == '__main__':

    def moving(x, y):
        t0.ht()
        t0.pu()
        t0.goto(x, y)
        t0.shape('circle')
        t0.stamp()
        t0.st()

    t0.ht()
    t0.speed(6)
    t0.width(8)
    t0.pu()
    t0.goto(xl, 0)
    t0.st()
    t0.pd()

    for i, c in enumerate(colors):
        t0.color(c)
        t0.write(c, font=font)
        s0.title(f'Проверяем работоспособность модуля...Всего цветов -> {n_colors - i} -> рисуем {c}')
        t0.circle(40)
        t0.goto(xl + 50 * (i + 1), 0)

    t0.color('maroon')
    t0.home()

    s0.title('Рисуем окружность, а затем меняем цвет фона!')
    t0.color('gold')
    t0.circle(100)

    s0.title('Меняем цвет фона...и рисуем большую окружность')
    s0.bgcolor('peru')
    t0.width(5)
    t0.rt(180)
    t0.circle(200)
    t0.rt(90)
    t0.color('burlywood')
    s0.title('Рисуем ушки...')
    t0.circle(30)
    t0.rt(180)
    t0.circle(30)
    s0.title('Меняем цвет фона... на серый! И рисуем *большие* черные уши!')
    s0.bgcolor('gray')
    t0.color('black')
    t0.circle(120)
    t0.rt(180)
    t0.circle(120)
    s0.title('Расставляем точки над ё...')
    moving(xl, yu)
    moving(xr, yu)
    moving(xl, yd)
    moving(xr, yd)

    s0.title('Для завершения - кликнете на экран')
    s0.exitonclick()
