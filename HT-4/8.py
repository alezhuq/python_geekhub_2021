# 8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
# Тобто, функція приймає два аргументи: список і величину зсуву
# (якщо ця величина додатня - пересуваємо з кінця на початок,
# якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
#    Наприклад:
#        fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#        fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]


def my_shift(a: list, shft: int):
    a = a[shft:] + a[:shft]
    return a


user_inp_list = input("input your values (e.g. :1, 2, 3, a, ...)").split(sep=", ")
user_shift = int(input("input your shift number : "))

new_list = my_shift(user_inp_list, user_shift)
print(new_list)
