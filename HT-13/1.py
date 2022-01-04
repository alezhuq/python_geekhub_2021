# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи.
#    Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
#    - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
#    - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
#    - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )


class Calc(object):
    """

    a class that represents a small copy of a calculator

    ...

    Attributes:
    static variables:
    last_result :float
        field for saving last computed result(default=None)

    instance variables:
    value: float
        field for storing a real number(default=0.0)

    Methods:
    static:
    get_last_result():
        :returns the value of variable last_result

    instance:
    get_value(self):
        :returns instance's value of variable value


    """

    last_result = None

    def __init__(self, value=0.0):
        """
        constructs value attribute for the object

        :parameter value :int, float
            a number that will be storing inside the object(default=0)

        """
        self.value = value

    @staticmethod
    def get_last_result() -> float:
        return Calc.last_result

    def get_value(self) -> float:
        return self.value

    def __add__(self, other):
        """
        overloads addition of 2 elements

        :param other :int, float or Calc
            value or another instance of a class that will be used for addition

        :return:
            new Calc object

        """

        if type(other) == int or type(other) == float:
            Calc.last_result = self.value + other
            return Calc(self.value + other)
        elif isinstance(other, Calc):
            Calc.last_result = self.value + other.value
            return Calc(self.value + other.value)

    def __sub__(self, other):
        """
        overloads subtraction of 2 elements

        :param other :int, float or Calc
            value or another instance of a class that will be used for subtraction

        :return:
            new Calc object

        """
        if type(other) == int or type(other) == float:
            Calc.last_result = self.value - other
            return Calc(self.value - other)
        elif isinstance(other, Calc):
            Calc.last_result = self.value - other.value
            return Calc(self.value - other.value)

    def __mul__(self, other):
        """
        overloads multiplication of 2 elements

        :param other :int, float or Calc
            value or another instance of a class that will be used for multiplication

        :return:
            new Calc object

        """
        if type(other) == int or type(other) == float:
            Calc.last_result = self.value * other
            return Calc(self.value * other)
        elif isinstance(other, Calc):
            Calc.last_result = self.value * other.value
            return Calc(self.value * other.value)

    def __truediv__(self, other):
        """
        overloads division of 2 elements

        :param other :int, float or Calc
            value or another instance of a class that will be used for division

        :return:
            new Calc object

        """
        if type(other) == int or type(other) == float and other:
            Calc.last_result = self.value / other
            return Calc(self.value / other)
        elif isinstance(other, Calc) and other.value:
            Calc.last_result = self.value / other.value
            return Calc(self.value / other.value)


def main():
    a = Calc(5)
    b = Calc(4)
    print("created a and b with values 5 and 4 correspondingly")

    c = a + b
    print("after addition a + b : ", c.get_value())

    c += b
    print("getting last calculated result (c+=b): ", Calc.get_last_result())

    d = a / b
    print("printing last result and res of d = a/b(should be equal) : ", Calc.get_last_result(), "; ", d.get_value())

    m = d + 5
    print("last result after m = d+5 : ", Calc.get_last_result())

    m = m * 2
    print("value of m after multiplying by 2 : ", m.get_value())


if __name__ == "__main__":
    main()
