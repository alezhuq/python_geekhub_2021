# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#    - щось своє :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.


class LenException(Exception):
    def __init__(self, message):
        self.message = message


class NoNumberException(Exception):
    def __init__(self, message = "you have to write at least 1 number"):
        self.message = message


def user_validation(username, password:str):

    if not 3 <= len(username) <= 50:
        raise LenException("the length of a username does not satisfy the conditions  3<= length <=50")
    if len(password) < 8:
        raise LenException("the length of a password does not satisfy the conditions  password  >= 8")
    for i in password:
        if i.isdigit():
            break
    else:
        raise NoNumberException()

    print("good username and password")


usr_nickname, usr_pass = input("input your login and password (ex :login password) : ").split(sep=" ")

user_validation(usr_nickname, usr_pass)
