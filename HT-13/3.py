# 3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white
# і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__
# для задання початкових розмірів об'єктів при їх створенні.


class Figure(object):
    color = "white"

    def set_color(self, new_color):
        self.color = new_color


class Oval(Figure):

    def __init__(self, small_axis: float, big_axis: float):
        self.small_axis = small_axis
        self.big_axis = big_axis


class Square(Figure):
    def __init__(self, side: float):
        self.side = side


def main():
    new_oval = Oval(2, 4)
    new_oval.set_color("blue")
    print(new_oval.color)
    new_square = Square(5)
    print(new_square.color)


if __name__ == "__main__":
    main()
