from turtle import exitonclick, title, width, color, begin_fill, end_fill, circle, lt, up, fd, rt, ht, backward, down,\
    reset


def yin(radius, color1, color2):
    width(3)
    color("black", color1)
    begin_fill()
    circle(radius / 2., 180)
    circle(radius, 180)
    lt(180)
    circle(-radius / 2., 180)
    end_fill()
    lt(90)
    up()
    fd(radius * 0.35)
    rt(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius * 0.15)
    end_fill()
    lt(90)
    up()
    backward(radius * 0.35)
    down()
    lt(90)


def main():
    reset()
    ht()
    title('Строим Инь!')
    yin(200, "black", "white")
    title('Строим Янь!')
    yin(200, "white", "black")
    return title('Построение закончено! Кликнете окно для Выхода!')


if __name__ == '__main__':
    main()
    exitonclick()
