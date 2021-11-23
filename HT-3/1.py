# 1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову,
#    яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.

def remainder_of_seventeen(n):
    for i in range(1, n + 1):
        if not i % 17:
            print(i)


user_input = int(input("input a positive integer : "))

remainder_of_seventeen(user_input)
