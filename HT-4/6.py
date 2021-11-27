# 6. Вводиться число. Якщо це число додатне, знайти його квадрат,
# якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.


def custom_func(number):
    if number > 0:
        number *= number

    elif number < 0:
        number += 100

    return number


usr_inp = int(input("input an integer : "))
print(custom_func(usr_inp))
