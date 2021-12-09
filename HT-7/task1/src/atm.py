# 1. Програма-банкомат.
#    Створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>); done
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>)
#       та історію транзакцій (файл <{username}_transactions.data>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних
#       (введено число; знімається не більше, ніж є на рахунку).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається.
#       Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - спочатку - логін користувача - програма запитує ім'я/пароль.
#       Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
#       (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#       - потім - елементарне меню типа:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив :)

from pathlib import Path
from datetime import datetime
import json


def validate_user(username: str, password: str) -> bool:
    # checks if pair user/password is in file users.data :
    with open(Path(__file__).parent.parent / "data" / "users.data") as users_data:
        for user_line in users_data.readlines():
            name, secur = user_line[:-1].split(sep=" ")
            if name == username and secur == password:
                return True
        else:
            return False


def make_transaction(username : str, amount : float):
    # changes {username}_balance.data on {amount} and saves operation in json ("d/m/y h:m:s": amount)
    with open(Path(__file__).parent.parent / "data" / f"{username}_balance.data") as data_content:
        balance = float(data_content.readlines()[0])

    if amount + balance < 0:
        print("can't perform the operation")
        return

    balance += amount

    with open(Path(__file__).parent.parent / "data" / f"{username}_balance.data", "w") as data_content:
        data_content.write(str(balance))

    transaction_dict = {datetime.now().strftime("%d/%m/%Y %H:%M:%S"): amount}

    with open(Path(__file__).parent.parent / "data" / f"{username}_transactions.data", "a") as transactions:
        transactions.write(json.dumps(transaction_dict))
    print("Succesful operation")


def view_balance(username : str):
    # shows the current balance of a user
    with open(Path(__file__).parent.parent / "data" / f"{username}_balance.data") as data_content:
        print(float(data_content.readlines()[0]))


def start():
    # main function, runs all mentioned above
    ok = True
    while ok:
        username, password = input("enter your username and password(ex. :antoxaMC mypasswrd) : ").split(sep=" ")
        if not validate_user(username, password):
            print("bad username or password")
            break
        flag = True
        while flag:
            choice = int(input(
                '''Введіть дію:\n1. Продивитись баланс\n2. Поповнити баланс\n3. Вихід\n(example : 1) : '''
            ))
            if choice == 1:
                view_balance(username)
            elif choice == 2:
                amount = float(input("input your sum (+ = addition, - = substraction)"))
                make_transaction(username, amount)
            elif choice == 3:
                flag = False

        answer = input("continue?(y/n) : ")
        if answer == "n":
            ok = False


if __name__ == "__main__":
    start()




