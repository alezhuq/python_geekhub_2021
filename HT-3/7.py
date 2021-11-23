# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calc(a, sign, b):
    if sign == "+":
        result = a+b
    elif sign == "-":
        result = a-b
    elif sign == "*":
        result = a*b
    elif sign == "/":
        if b:
            result = a/b
        else :
            result = "can't divide by zero :("
    else:
        result = "unsupported operation"
    return result


print("CURRENTLY SUPPORTED OPERATIONS : +, -, *, /")
first, sign, second = str(input("input what you want to calculate (ex :13 + 15) : ")).split(sep = " ")
print(calc(int(first), sign, int(second)))