# 2. Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
#    - Перелік валют краще принтануть.
#    - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
#    - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
#    - Також перевірте, чи введена правильна валюта.
#    Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
#    курсу обраної валюти (Нацбанк) від введеної дати до поточної.:


import requests
import datetime as dt
import time


def get_possible_currencies(user_date):
    try:
        request = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={user_date}&json")
        request.raise_for_status()
    except:
        print("can't connect to the server now, try again later")
        return

    print("all possible currencies(a lot)")
    for currency_dict in request.json():
        print(f"{currency_dict['txt']} : {currency_dict['cc']}")
    time.sleep(0.5)


def get_all_courses_for_currency(user_curr, user_date):
    delta = dt.timedelta(days=1)
    date1 = dt.datetime.strptime(user_date, "%Y%m%d")
    print(f"Currency : {user_curr}")
    change = "------"
    while date1 < dt.datetime.now():
        try:
            request = requests.get(
                f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={user_date}&json")
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
        user_date = str(dt.datetime.strftime(date1, "%Y%m%d"))
        show_date = str(dt.datetime.strftime(date1, "%d.%m.%Y"))
        print("Date : ", show_date)
        if type(change) is str:
            print("NBU: ", my_dict['rate'], change)

        else:
            print("NBU: ", my_dict['rate'], my_dict['rate'] - change)
        change = my_dict['rate']

        date1 += delta
        time.sleep(0.5)



if __name__ == "__main__":
    user_input = input("input the currency starting date(ex :17.12.2021): ")
    try:
        user_date = dt.datetime.strftime(dt.datetime.strptime(user_input, "%d.%m.%Y"), "%Y%m%d")

    except ValueError:
        user_date = str(dt.datetime.strftime(dt.datetime.now(), "%Y%m%d"))
        print("incorrect date, setting to current")

    except Exception:
        print("something is wrong")
        exit(1)

    if user_date > str(dt.datetime.strftime(dt.datetime.now(), "%Y%m%d")):
        print("i think it's the future")
        exit(1)

    get_possible_currencies(user_date)

    user_input = input("input the currency (all capitals, ex :USD) : ")

    try:
        user_curr = user_input.upper()

    except ValueError:
        user_curr = "USD"
        print("incorrect name, setting to default : USD")

    except Exception:
        print("something is wrong")
        exit(1)

    get_all_courses_for_currency(user_curr, user_date)
