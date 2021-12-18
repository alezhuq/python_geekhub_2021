# 3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
#    Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
#    конвертацію введеної суми з однієї валюти в іншу.

import requests
import datetime as dt
import time


def get_possible_currencies():
    curr_date = str(dt.datetime.strftime(dt.datetime.now(), "%Y%m%d"))

    try:
        request = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={curr_date}&json")
        request.raise_for_status()
    except:
        print("can't connect to the server now, try again later")
        return

    print("all possible currencies(a lot)")
    for currency_dict in request.json():
        print(f"{currency_dict['txt']} : {currency_dict['cc']}")
    time.sleep(0.5)


def find_user_currency(user_curr):
    curr_date = str(dt.datetime.strftime(dt.datetime.now(), "%Y%m%d"))
    try:
        request = requests.get(
            f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={curr_date}&json")
        request.raise_for_status()

    except:
        print("can't connect to the server now, try again later")
        return

    my_dict = {}

    for i in request.json():
        i.setdefault("message", 0)
        if i["message"]:
            print("something is bad")
            return
        if i["cc"] == user_curr:
            my_dict = i
            break

    if not my_dict:
        print("can't find the currency")
        return
    time.sleep(0.5)

    return my_dict


def convert(user_curr1, user_curr2, user_sum):
    if user_curr1 == user_curr2:
        res = user_sum

    elif user_curr1 == "UAH":
        curr_dict2 = find_user_currency(user_curr2)
        res = float(user_sum)/curr_dict2['rate']

    elif user_curr2 == "UAH":
        curr_dict1 = find_user_currency(user_curr1)
        res = float(user_sum) * curr_dict1['rate']

    else:
        curr_dict1 = find_user_currency(user_curr1)
        curr_dict2 = find_user_currency(user_curr2)
        res = float(user_sum) * curr_dict1['rate'] / curr_dict2['rate']

    return res


if __name__ == "__main__":
    get_possible_currencies()

    user_input = input("input your currencies (, ex :USD, EUR) : ")


    try:
        user_curr1, user_curr2 = user_input.split(sep=", ")
        user_curr1, user_curr2 = user_curr1.upper(), user_curr2.upper()

    except ValueError:
        user_curr1 = "USD"
        user_curr2 = "UAH"
        print("incorrect name, setting to default : USD, UAH")

    except Exception:
        print("something is wrong")
        exit(1)

    user_sum = input(f"input your sum for the{user_curr1} : ")
    try:
        user_sum = float(user_sum)
    except ValueError:
        user_sum = 100
        print("incorrect value, setting to default : 100")

    result = convert(user_curr1, user_curr2, user_sum)

    print(round(result, 3))
