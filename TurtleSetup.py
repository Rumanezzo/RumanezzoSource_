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
x_right = s0.window_width() // 2 - step  # Самая правая
x_left = -x_right  # Самая левая
y_up = s0.window_height() // 2 - step  # Самая верхняя
y_down = -y_up  # Самая нижняя

s0.bgcolor('grey')
# -------------------------------Конец инициализации экрана-------------------------------

colors = (
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "violet", "aquamarine",
    "bisque", "burlywood", "chartreuse", "magenta", "moccasin", "navy", "plum", "tan",
    "thistle", "turquoise", "tomato", "brown", "salmon", "gold", "maroon", "sienna",
    "peru", "lightgreen", "cyan",)

n_colors = len(colors)

if __name__ == '__main__':

    def moving(coord_x, coord_y, color):
        t0.ht()
        t0.pu()
        t0.goto(coord_x, coord_y)
        t0.color(color)
        t0.shape('circle')
        t0.stamp()
        t0.st()

    t0.ht()
    t0.speed(6)
    t0.width(8)
    t0.pu()
    t0.goto(x_left, 0)
    t0.st()
    t0.pd()

    title_output = '⋅'
    for i, c in enumerate(colors):
        t0.color(c)

        title_output += f'{c}⋅'
        s0.title(title_output)
        t0.circle(40)
        t0.bk(40)
        if i % 2:
            t0.lt(90)
        else:
            t0.rt(90)
        t0.fd(40)
        t0.write(c, font=font)
        t0.goto(x_left + 50 * (i + 1), 0)

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
    t0.color('chartreuse')
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
    moving(x_left, y_up, 'yellow')
    moving(x_right, y_up, 'green')
    moving(x_left, y_down, 'cyan')
    moving(x_right, y_down, 'magenta')

    s0.title('Для завершения - кликнете на экран')
    s0.exitonclick()
