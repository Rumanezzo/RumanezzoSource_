import turtle as t0


def star(t, n, r):
    for k in range(0, n):
        t.pendown()
        t.forward(r)
        t.penup()
        t.backward(r)
        t.left(360 / n)


def recursive_star(t, n, r, depth, f):
    if depth == 0:
        star(t, n, f * 4)
    else:
        for k in range(0, n):
            t.pendown()
            t.forward(r)
            recursive_star(t, n, f * r, depth - 1, f)
            t.penup()
            t.backward(r)
            t.left(360 / n)


t0.speed(0)
t0.ht()
recursive_star(t0, 5, 150, 4, 0.4)
t0.done()
