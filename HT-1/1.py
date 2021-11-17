# 1 .Write a script which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.


user_input = str(input("input your numbers (ex : 1, 2, 3):"))

out_list = user_input.split(sep=", ")
out_tuple = tuple(out_list)

print(out_list, "\n", out_tuple)