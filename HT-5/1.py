# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#    Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій
#    - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#    Логіка наступна:
#        якщо введено коректну пару ім'я/пароль - вертається <True>;
#        якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
#        інакше (<silent> == <False>) - породжується виключення LoginException


class LoginException(Exception):
    def __init__(self):
        print("YOU SHALL NOT PASS")


def log_in(username, password, silent=False):
    dataset_of_accounts = [
        {
            "Al1n04ka15": "i_like_cats",
            "login": "password",
            "Groovy": "idkidkidk",
            "YaPasha": "322",
            "Crypto_investor": "HODL_SHIB"
        }
    ]

    if username in dataset_of_accounts[0].keys() and dataset_of_accounts[0][username] == password:
        ok = True

    else:
        ok = False
    if not silent:
        raise LoginException
    return ok


usr_nickname, usr_pass = input("input your login and password (ex :login password) : ").split(sep=" ")
check_admin = input("are you admin?(y/n)")
if check_admin == "y":
    print(log_in(usr_nickname, usr_pass, True))
else:
    print(log_in(usr_nickname, usr_pass))