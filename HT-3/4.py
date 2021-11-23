# 4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
#    Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi,
#    обробляє повернутий ними результат та також повертає результат.
#    Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def add_1(x):
    return x + 1


def is_positive(x):
    return x >= 0


def is_odd(x):
    return x % 2


def custom_func(x):
    if is_positive(x):
        print("your value is positive")
    else:
        print("your value is negative")
    if is_odd(x):
        x = add_1(x)
        print("changed your value to even")
    return x


user_input = int(input("input an integer : "))

user_input = custom_func(user_input)
