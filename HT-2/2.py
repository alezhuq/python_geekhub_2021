# 2. Написати скрипт, який пройдеться по списку, який складається із кортежів,
#    і замінить для кожного кортежа останнє значення.
#    Список із кортежів можна захардкодити.
#    Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
#    Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком).
#    Кількість елементів в кортежу повинна бути різна.

hardcoded_list_of_sets = [(20, 40, 80), (160, 320, 640, 1280), (2560,)]

user_input = input("input a number : ")

for i in range(len(hardcoded_list_of_sets)):
    temp_element = list(hardcoded_list_of_sets[i])
    temp_element.pop()
    temp_element.append(user_input)
    hardcoded_list_of_sets[i] = tuple(temp_element)

print(hardcoded_list_of_sets)

