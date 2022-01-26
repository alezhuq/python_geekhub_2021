# Використовуючи бібліотеку requests
# написати скрейпер для отримання статей / записів із АПІ

# Документація на АПІ:
# https://github.com/HackerNews/API

# Скрипт повинен отримувати із командного рядка одну із наступних категорій:

# askstories, showstories, newstories, jobstories

# Якщо жодної категорії не указано - використовувати newstories.
# Якщо категорія не входить в список - вивести попередження про це
# і завершити роботу.
# Результати роботи зберегти в CSV файл.
# Зберігати всі доступні поля.
#
# Зверніть увагу - інстанси різних типів мають різний набір полів.
# Код повинен притримуватися стандарту pep8.

import csv

from pathlib import Path
from time import sleep

import requests


def category_getter():
    list_of_allowed_categories = [
        "askstories",
        "showstories",
        "newstories",
        "jobstories"
    ]
    print("supported categories :\n", list_of_allowed_categories)
    category = input("input your category : ")

    res = None

    if category in list_of_allowed_categories:
        res = category
    elif category == "":
        print("setting category to default(newstories)")
        res = "newstories"
    return res


def get_all_ids(category, base_url):
    data_format = ".json"
    if category:
        try:
            request = requests.get(base_url + category + data_format)
            request.raise_for_status()
            sleep(0.5)
        except Exception as e:
            print("there was a problem with getting info from your page", e)
            return
    else:
        return

    return request.json()


def get_items_and_write_csv(id_list, base_url):
    data_format = ".json"
    temp_url = base_url + "item/"
    all_fields = ["by",
                  "descendants",
                  "kids",
                  "id",
                  "score",
                  "time",
                  "title",
                  "type",
                  "url"
                  ]

    with open(Path(Path.cwd() / "file.csv"), "w") as f:
        writer = csv.writer(f)
        writer.writerow(all_fields)

    for element in id_list:
        try:
            request = requests.get(temp_url + str(element) + data_format)
            request.raise_for_status()

        except Exception as e:
            print("there was a problem with getting info from your page", e)
            return

        temp_item = request.json()

        for attribute in all_fields:
            temp_item.setdefault(attribute, "None")

        temp_item = dict(sorted(temp_item.items()))

        with open(Path(Path.cwd() / "file.csv"), "a") as f:
            writer = csv.writer(f)
            writer.writerow(temp_item.values())

        print("current item : ", temp_item)


def start():
    base_url = "https://hacker-news.firebaseio.com/v0/"
    user_category = category_getter()

    print(user_category)

    id_list = get_all_ids(user_category, base_url)
    if id_list:
        get_items_and_write_csv(id_list, base_url)


if __name__ == "__main__":
    start()
