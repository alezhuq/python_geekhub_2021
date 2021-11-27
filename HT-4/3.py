# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
# i яка вертатиме True, якщо це число просте, i False - якщо ні.

from math import sqrt


def is_prime(number):
    ok = True
    for i in range(2, int(sqrt(number))+1):
        if not number % i:
            ok = False
            break

    return ok


usr_inp = int(input("input your int number : "))
res = is_prime(usr_inp)
print(res)
