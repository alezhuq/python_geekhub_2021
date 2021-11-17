# 6. Write a script to check whether a specified value is contained in a group of values.

input_str = str(input("input your list of values (ex : 1, 2, 3) : "))

check_list = input_str.split(sep=", ")


input_value = str(input("input your specified value : "))


if input_value in check_list:
    print(True)
else:
    print(False)


