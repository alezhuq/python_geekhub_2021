# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
#    https://docs.python.org/3/library/stdtypes.html#range


def my_cutom_range(number: int):
    i = 0
    while i < number:
        yield i
        i += 1


print(type(my_cutom_range(5)))

for i in my_cutom_range(5):
    print(i)

