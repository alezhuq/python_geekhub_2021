# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.


def fibonacci(number):
    fib1 = 0
    fib2 = 1
    if fib1 < number:
        print(fib1)
    if fib2 < number:
        print(fib2)
    fib3 = fib1+fib2
    while fib3 < number:
        print(fib3)
        fib1, fib2 = fib2, fib3
        fib3 = fib1 + fib2


usr_inp = int(input("input a positive integer : "))
fibonacci(usr_inp)
