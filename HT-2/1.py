# 1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран.
#    Список можна "захардкодити".
#    Елементами списку повинні бути як рядки, так і числа.

hardcoded_list = [1, ". write a script with at least ", 1, " number and ", 1.5, " strings okei?"]

hardcoded_string_list = list(str(i) for i in hardcoded_list)

res_string = "".join(hardcoded_string_list)
print(res_string)




