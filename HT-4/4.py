# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона.

from math import sqrt


# func from task 3
def is_prime(number):
    ok = True
    for i in range(2, int(sqrt(number)) + 1):
        if not number % i:
            ok = False
            break

    return ok


def prime_list(beg, end):
    return list(i for i in range(beg, end+1) if is_prime(i))  # exclusive range (with beg and end).


usr_beg, usr_end = input("input the start and end of your range (e.g. :10, 20) : ").split(sep=", ")
usr_beg, usr_end = int(usr_beg), int(usr_end)

print(prime_list(usr_beg, usr_end))