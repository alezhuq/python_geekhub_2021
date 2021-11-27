# 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж):
# периметр квадрата, площа квадрата та його діагональ.

from math import sqrt


def square(side):
    return side * 4, side * side, side * sqrt(2)  # периметр, площа, діагональ


usr_inp = float(input("input the side of a square (may be real number, but not negative) : "))
res = square(usr_inp)
print("perimeter : {}, area : {}, diagonal : {}".format(res[0], res[1], res[2]))
