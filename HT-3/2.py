# 2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).


def print_leaps(beg, end):
    for i in range(beg, end + 1):
        if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
            print(i)


beg_yr, end_yr = input("input start and end year(ex :1999, 2020) : ").split(sep=", ")

print_leaps(int(beg_yr), int(end_yr))