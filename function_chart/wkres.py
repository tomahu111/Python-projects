import turtle

rysownik_wykresu=turtle.Turtle()

rysownik_wykresu.forward(1000)
rysownik_wykresu.backward(2000)
rysownik_wykresu.forward(1000)
rysownik_wykresu.lt(90)
rysownik_wykresu.forward(1000)
rysownik_wykresu.backward(2000)
rysownik_wykresu.forward(1000)
rysownik_wykresu.rt(45)


def rysowanie(ix, iy):
    rysownik_wykresu.goto(ix, iy)
