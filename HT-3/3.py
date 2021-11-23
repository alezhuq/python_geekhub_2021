# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)


def season(num):
    if  3 <= num <= 5:
        print("Spring")

    elif 6 <= num <= 8:
        print("Summer")

    elif 9 <= num <= 11:
        print("Fall")

    elif num in [12, 1, 2]:
        print("Winter")
    else:
        print("idk")

us_inp = int(input("inp your int number : "))
season(us_inp)