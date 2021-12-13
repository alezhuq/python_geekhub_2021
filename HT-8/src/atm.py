# 1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
#    Отже, у банкомата повинен бути такий режим як "інкассація",
#    за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
#    Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом -
#    видається мінімальна кількість банкнот наявного номіналу.
#    P.S. Будьте обережні з використанням "жадібного" алгоритму
#    (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) -
#    в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн.,
#    а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму
#    (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
#    Особливості реалізації:
#    - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
#    - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
#      - переглянути наявні купюри;
#      - змінити кількість купюр;
#    - видача грошей для користувачів відбувається в межах наявних купюр;
#    - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й,
#    наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
# 2. Для кращого засвоєння - перед написанням коду із п.1 -
#    видаліть код для старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).
#    До того ж, скоріш за все, вам прийдеться і так багато чого переписати.


from pathlib import Path
from datetime import datetime
import json


def validation(username: str, password: str):
    with open(Path(__file__).parent.parent / "data" / "users.data") as all_users:
        for user_line in all_users.readlines():
            try:
                name, secur, status = user_line[:-1].split(sep=" ")
            except Exception:
                print("invalid data")
                return "out"

            if name == username and secur == password:
                if status == "worker":
                    return "worker"
                return "no"


def give_money(nominals: dict, value: int):
    except_dict = {i: 0 for i in nominals.keys()}
    for i in reversed(nominals.keys()):
        while value - int(i) >= 0 and nominals[i] > 0:
            value = value - int(i)
            except_dict[i] += 1
            nominals[i] -= 1
    if not value == 0:
        for i in nominals.keys():
            if except_dict[i] > 0:
                nominals[i] += except_dict[i]
        return False
    else:
        with open(Path(__file__).parent.parent / "data" / "atm.data", "wt") as atm_nominal:
            atm_nominal.write(json.dumps(nominals))
        return True


def money_in(username: str, amount: int):
    if amount <= 0:
        print("incorrect value")
        return
    with open(Path(__file__).parent.parent / "data" / f"{username}_balance.data") as balance:
        total_dinero = amount + int(balance.read())
    with open(Path(__file__).parent.parent / "data" / f"{username}_balance.data", "wt") as user_file:
        user_file.write(str(total_dinero))

    transaction_dict = {datetime.now().strftime("%d/%m/%Y %H:%M:%S"): amount}
    with open(Path(__file__).parent.parent / "data" / f"{username}_transactions.data", "a") as transactions:
        transactions.write(json.dumps(transaction_dict))


def money_out(username: str, amount: int):
    if amount <= 0:
        print("incorrect value")
        return
    with open(Path(__file__).parent.parent / "data" / f"{username}_balance.data") as balance:
        total_dinero = int(balance.read()) - amount
    if (total_dinero) < 0:
        print("can't perform the operation")
        return
    else:
        with open(Path(__file__).parent.parent / "data" / "atm.data") as atm_nominal:
            nominals = json.loads(atm_nominal.read())

        if give_money(nominals, amount):
            with open(Path(__file__).parent.parent / "data" / f"{username}_balance.data", "wt") as user_file:
                user_file.write(str(total_dinero))

            transaction_dict = {datetime.now().strftime("%d/%m/%Y %H:%M:%S"): amount}
            with open(Path(__file__).parent.parent / "data" / f"{username}_transactions.data", "a") as transactions:
                transactions.write(json.dumps(transaction_dict))
            print("operation good")
        else:
            print("can't do it rn, sry")


def cash_out():
    with open(Path(__file__).parent.parent / "data" / "atm.data") as atm_nominal:
        nominals = json.loads(atm_nominal.read())
    for i in nominals.keys():
        nominals[i] = 0
    with open(Path(__file__).parent.parent / "data" / "atm.data", "wt") as atm_nominal:
        atm_nominal.write(json.dumps(nominals))
    print("operation good")


def cash_in(nominal: int, amount: int):
    with open(Path(__file__).parent.parent / "data" / "atm.data") as atm_nominal:
        nominals = json.loads(atm_nominal.read())
    if not (str(nominal) in nominals.keys()):
        print("i don't hold such type of nominal")
        return
    if amount <= 0:
        print("dont scam me okei?")
        return
    else:
        nominals[str(nominal)] += amount
        with open(Path(__file__).parent.parent / "data" / "atm.data", "wt") as atm_nominal:
            atm_nominal.write(json.dumps(nominals))
        print("operation good")


def view_balance(username: str):
    # shows the current balance of a user
    with open(Path(__file__).parent.parent / "data" / f"{username}_balance.data") as data_content:
        print(int(data_content.readlines()[0]))


def view_atm():
    with open(Path(__file__).parent.parent / "data" / "atm.data") as atm_nominal:
        nominals = json.loads(atm_nominal.read())
    print(nominals)


def start():
    # main function, runs all mentioned above
    ok = True
    while ok:
        username, password = input("enter your username and password(ex.:antoxaMC mypasswrd) : ").split(sep=" ")
        valid_res = validation(username, password)
        if valid_res == "out":
            print("bad username or password")
            break
        elif valid_res == "no":
            flag = True
            while flag:
                choice = int(input(
                    '''Actions:\n1.view balance\n2. money in\n3. money out\n4. exit\n(example : 1) : '''
                ))
                if choice == 1:
                    view_balance(username)
                elif choice == 2:
                    amount = int(input("input your sum :"))
                    money_in(username, amount)
                elif choice == 3:
                    amount = int(input("input your sum (but with plus) :"))
                    money_out(username, amount)
                elif choice == 4:
                    flag = False
        elif valid_res == "worker":
            flag = True
            while flag:
                choice = int(input(
                    '''Actions:\n1.view balance\n2. cash in\n3. cash out\n4. exit\n(example : 1) : '''
                ))
                if choice == 1:
                    view_atm()
                elif choice == 2:
                    nominal = int(input("input your nominal :"))
                    amount = int(input("input your amount :"))
                    cash_in(nominal, amount)
                elif choice == 3:
                    cash_out()
                elif choice == 4:
                    flag = False
        else:
            print("bad uname/password")
        answer = input("continue?(y/n) : ")
        if answer == "n":
            ok = False


if __name__ == "__main__":
    start()
