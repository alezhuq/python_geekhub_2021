# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
#    https://docs.python.org/3/library/stdtypes.html#range



def my_cutom_range(*args):
    if len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1
    else:
        start = 0
        end = args[0]
        step = 1

    while start < end:
        yield start
        start += step


print(type(my_cutom_range(5)))

for i in my_cutom_range(5):
    print(i)

