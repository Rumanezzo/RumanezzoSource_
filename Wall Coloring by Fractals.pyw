from turtle import Turtle, Screen, exitonclick
from time import perf_counter as clock


class Designer(Turtle):

    def design(self, home_pos, scale):
        self.up()
        for i in range(5):
            self.fd(64.65 * scale)
            self.down()
            self.wheel(self.position(), scale)
            self.up()
            self.backward(64.65 * scale)
            self.rt(72)
        self.up()
        self.goto(home_pos)
        self.rt(36)
        self.fd(24.5 * scale)
        self.rt(198)
        self.down()
        self.centerpiece(46 * scale, 143.4, scale)
        self.getscreen().tracer(True)

    def wheel(self, init_pos, scale):
        self.rt(54)
        for i in range(4):
            self.pent_piece(init_pos, scale)
        self.down()
        self.left(36)
        for i in range(5):
            self.tri_piece(init_pos, scale)
        self.left(36)
        for i in range(5):
            self.down()
            self.right(72)
            self.forward(28 * scale)
            self.up()
            self.backward(28 * scale)
        self.lt(54)
        self.getscreen().update()

    def tri_piece(self, init_pos, scale):
        old_head = self.heading()
        self.down()
        self.backward(2.5 * scale)
        self.tri_poly_rt(31.5 * scale, scale)
        self.up()
        self.goto(init_pos)
        self.setheading(old_head)
        self.down()
        self.backward(2.5 * scale)
        self.tri_poly_lt(31.5 * scale, scale)
        self.up()
        self.goto(init_pos)
        self.setheading(old_head)
        self.left(72)
        self.getscreen().update()

    def pent_piece(self, init_pos, scale):
        old_head = self.heading()
        self.up()
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        self.pent_rt(18 * scale, 75, scale)
        self.up()
        self.goto(init_pos)
        self.setheading(old_head)
        self.fd(29 * scale)
        self.down()
        for i in range(5):
            self.fd(18 * scale)
            self.rt(72)
        self.pent_lt(18 * scale, 75, scale)
        self.up()
        self.goto(init_pos)
        self.setheading(old_head)
        self.lt(72)
        self.getscreen().update()

    def pent_lt(self, side, ang, scale):
        if side < (2 * scale):
            return
        self.fd(side)
        self.lt(ang)
        self.pent_lt(side - (.38 * scale), ang, scale)

    def pent_rt(self, side, ang, scale):
        if side < (2 * scale):
            return
        self.fd(side)
        self.rt(ang)
        self.pent_rt(side - (.38 * scale), ang, scale)

    def tri_poly_rt(self, side, scale):
        if side < (4 * scale):
            return
        self.fd(side)
        self.rt(111)
        self.fd(side / 1.78)
        self.rt(111)
        self.fd(side / 1.3)
        self.rt(146)
        self.tri_poly_rt(side * .75, scale)

    def tri_poly_lt(self, side, scale):
        if side < (4 * scale):
            return
        self.fd(side)
        self.lt(111)
        self.fd(side / 1.78)
        self.lt(111)
        self.fd(side / 1.3)
        self.lt(146)
        self.tri_poly_lt(side * .75, scale)

    def centerpiece(self, s, a, scale):
        self.fd(s)
        self.lt(a)
        if s < (7.5 * scale):
            return
        self.centerpiece(s - (1.2 * scale), a, scale)


def main():
    t = Designer()
    s = Screen()
    s.setup(0.99, 0.9, 0, 0)
    s.title('Рисуем несколько фракталов...')
    t.speed(0)
    t.ht()
    t.getscreen().delay(0)
    t.getscreen().tracer(0)
    at = clock()
    for i in range(2):
        t.design(t.position(), 8)
        t.rt(90)

    et = clock()
    s.title(f'Фрактал - время прорисовки: {(et - at):.2f} сек. - работа завершена!')


if __name__ == '__main__':
    main()
    exitonclick()
