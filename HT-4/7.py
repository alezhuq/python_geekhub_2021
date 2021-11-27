# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.


def my_counter(usr_list):
    count_dict = {i: usr_list.count(i) for i in usr_list}
    print(count_dict)


usr_inp = (input("input your values (e.g. :1, 2, 3, a, ...)")).split(sep=", ")
my_counter(usr_inp)