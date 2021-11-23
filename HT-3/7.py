# 7. Ну і традиційно -> калькулятор :)
#    повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!


def calculate(a, sign, b):

    if sign == "+":
        result = a + b
    elif sign == "-":
        result = a - b
    elif sign == "*":
        result = a * b
    elif sign == "/":
        result = a / b
    else:
        result = "cant perform your operation"
    return result

print("Current supported operations : +, -, *, /")
first, sign, second = input("input your equasion (ex:14 + 15) : ").split(sep=" ")
first = int(first)
second = int(second)

print(calculate(first, sign, second))

