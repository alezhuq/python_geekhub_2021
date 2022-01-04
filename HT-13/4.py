# 4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури»
# та приймав колір фігури при створенні екземпляру, а методи __init__ підкласів доповнювали його
# та додавали початкові розміри.


class Figure(object):
    def __init__(self, color="white"):
        self.color = color

    def set_color(self, new_color):
        self.color = new_color


class Oval(Figure):

    def __init__(self, small_axis: float, big_axis: float, color="white"):
        super().__init__(color)
        self.small_axis = small_axis
        self.big_axis = big_axis


class Square(Figure):
    def __init__(self, side: float, color="white"):
        super().__init__(color)
        self.side = side


def main():
    new_oval = Oval(2, 4, "red")
    print(new_oval.color)
    new_square = Square(5)
    print(new_square.color)


if __name__ == "__main__":
    main()
