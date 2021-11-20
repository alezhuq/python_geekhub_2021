# 8. Написати скрипт, який отримує від користувача позитивне ціле число
#    і створює словник, з ключами від 0 до введеного числа,
#    а значення для цих ключів - це квадрат ключа.


user_int = int(input("input a positive number : "))

new_dict = {i: i*i for i in range(user_int+1)}

print(new_dict)
