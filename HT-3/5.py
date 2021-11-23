# 5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# -  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
# -  Повиннi опрацювати такi умови:
# -  x > y;       вiдповiдь - х бiльше нiж у на z
# -  x < y;       вiдповiдь - у бiльше нiж х на z
# -  x == y.      вiдповiдь - х дорiвнює z


def simp_construct(x, y):
    if x > y:
        print("{}(x) > {}(y) by {}".format(x, y, x-y))

    elif y > x:
        print("{}(y) > {}(x) by {}".format(y, x, y-x))

    else:
        print("{}(x) = {}(y)".format(x, y))


x, y = str(input("input your values(ex:14, 15)" )).split(sep = ", ")
simp_construct(int(x), int(y))
