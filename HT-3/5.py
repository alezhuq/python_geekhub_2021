# 5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
#    -  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
#       пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y"
#       і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
#       -  Повиннi опрацювати такi умови:
#            -  x > y;       вiдповiдь - х бiльше нiж у на z
#            -  x < y;       вiдповiдь - у бiльше нiж х на z
#            -  x == y.      вiдповiдь - х дорiвнює z


def simple_conditional_construction(x, y):
    if x > y:
        z = x-y
        print("Answer : {} (your x) is greater than {} (your y) by {}".format(x, y, z))

    elif y > x:
        z = y-x
        print("Answer : {} (your y) is greater than {} (your x) by {}".format(y, x, z))

    else:
        print("Answer : {} (your x) is equal to {} (your y)".format(x, y))


x = float(input("input your x (number) : "))
y = float(input("input your y (number) : "))

simple_conditional_construction(x, y)
