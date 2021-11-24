# 1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.


def my_func(n):
    for i in range(n):
        if i%17 == 0:
            print(i)

us_inp = int(input("inp your int number : "))
my_func(us_inp)
