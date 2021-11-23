# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
#    яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)


def season(number: int) -> str:
    my_str = ""
    if 3 <= number <= 5:
        my_str = "Spring"
    elif 6 <= number <= 8:
        my_str = "Summer"
    elif 9 <= number <= 11:
        my_str = "Fall"
    elif number in [12, 1, 2]:
        my_str = "Winter"
    else:
        my_str = "incorrect value"
    return my_str


user_input = int(input("input the number of the month (1-12) : "))
print(season(user_input))
