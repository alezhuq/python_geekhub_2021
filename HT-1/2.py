# 2. Write a script to print out a set containing all the colours
# from color_list_1 which are not present in color_list_2.

user_input = str(input("input color_list_1 (ex : white, black): "))
color_list_1 = set(user_input.split(sep=", "))

user_input = str(input("input color_list_2 (ex : white, black): "))
color_list_2 = set(user_input.split(sep=", "))

print(color_list_1-color_list_2)
