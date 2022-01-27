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
import sys

from pathlib import Path
from time import sleep

import requests


class Item(object):

    def __init__(self, by, id, score, time, title, type):
        self.by = by
        self.id = id
        self.score = score
        self.time = time
        self.title = title
        self.type = type

    @staticmethod
    def write_header(header_list):
        with open(Path(Path.cwd() / "file.csv"), "w") as f:
            writer = csv.writer(f)
            writer.writerow(header_list)

    @staticmethod
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


class Ask(Item):
    row = ["by", "id", "score", "time", "title", "type", "descendants", "kids", "text"]

    def __init__(self, by, descendants, id, kids, score, text, time, title, type):
        super().__init__(by, id, score, time, title, type)
        self.descendants = descendants
        self.kids = kids
        self.text = text

    def write_item(self):
        with open(Path(Path.cwd() / "file.csv"), "a") as f:
            writer = csv.writer(f)
            writer.writerow([self.by, self.id, self.score, self.time, self.title, self.type, self.descendants,
                             self.kids, self.text])


class New(Item):
    row = ["by", "id", "score", "time", "title", "type", "descendants", "kids", "text", "url"]

    def __init__(self, by, descendants, id, kids, score, text, time, title, type, url):
        super().__init__(by, id, score, time, title, type)
        self.descendants = descendants
        self.kids = kids
        self.text = text
        self.url = url

    def write_item(self):
        with open(Path(Path.cwd() / "file.csv"), "a") as f:
            writer = csv.writer(f)
            writer.writerow([self.by, self.id, self.score, self.time, self.title, self.type, self.descendants,
                             self.kids, self.text, self.url])


class Show(Item):
    row = ["by", "id", "score", "time", "title", "type", "descendants", "kids", "url"]

    def __init__(self, by, descendants, id, kids, score, url, time, title, type):
        super().__init__(by, id, score, time, title, type)
        self.descendants = descendants
        self.kids = kids
        self.url = url

    def write_item(self):
        with open(Path(Path.cwd() / "file.csv"), "a") as f:
            writer = csv.writer(f)
            writer.writerow([self.by, self.id, self.score, self.title, self.title, self.type, self.descendants,
                             self.kids, self.url])


class Job(Item):
    row = ["by", "id", "score", "time", "title", "type", "url"]

    def __init__(self, by, id, score, time, title, url, type):
        super().__init__(by, id, score, time, title, type)
        self.url = url
        self.type = "job"

    def write_item(self):
        with open(Path(Path.cwd() / "file.csv"), "a") as f:
            writer = csv.writer(f)
            writer.writerow([self.by, self.id, self.score, self.time, self.title, self.type, self.url])


def category_getter(usr_input):
    list_of_allowed_categories = [
        "askstories",
        "showstories",
        "newstories",
        "jobstories"
    ]

    res = None

    if usr_input in list_of_allowed_categories:
        res = usr_input
    elif usr_input == "":
        print("setting category to default(newstories)")
        res = "newstories"
    return res


def get_items_and_write_csv(category, id_list, base_url):
    data_format = ".json"
    temp_url = base_url + "item/"

    if category == "askstories":
        Ask.write_header(Ask.row)
    elif category == "showsotires":
        Show.write_header(Show.row)
    elif category == "jobstories":
        Job.write_header(Job.row)
    else:
        New.write_header(New.row)

    for element in id_list:
        try:
            request = requests.get(temp_url + str(element) + data_format)
            request.raise_for_status()

        except Exception as e:
            print("there was a problem with getting info from your page", e)
            return
        temp_item = request.json()
        if category == "askstories":
            object_to_write = Ask(
                by=temp_item.get("by", "None"),
                descendants=temp_item.get("descendants", "None"),
                id=temp_item.get("id", "None"),
                kids=temp_item.get("kids", "None"),
                score=temp_item.get("score", "None"),
                text=temp_item.get("text", "None"),
                time=temp_item.get("time", "None"),
                title=temp_item.get("title", "None"),
                type=temp_item.get("type", "None")
            )
        elif category == "showsotires":
            object_to_write = Show(
                by=temp_item.get("by", "None"),
                descendants=temp_item.get("descendants", "None"),
                id=temp_item.get("id", "None"),
                kids=temp_item.get("kids", "None"),
                score=temp_item.get("score", "None"),
                url=temp_item.get("url", "None"),
                time=temp_item.get("time", "None"),
                title=temp_item.get("title", "None"),
                type=temp_item.get("type", "None")
            )
        elif category == "jobstories":
            object_to_write = Job(
                by=temp_item.get("by", "None"),
                id=temp_item.get("id", "None"),
                score=temp_item.get("score", "None"),
                url=temp_item.get("url", "None"),
                time=temp_item.get("time", "None"),
                title=temp_item.get("title", "None"),
                type=temp_item.get("type", "None")
            )
        else:
            object_to_write = New(
                by=temp_item.get("by", "None"),
                descendants=temp_item.get("descendants", "None"),
                id=temp_item.get("id", "None"),
                kids=temp_item.get("kids", "None"),
                score=temp_item.get("score", "None"),
                url=temp_item.get("url", "None"),
                time=temp_item.get("time", "None"),
                title=temp_item.get("title", "None"),
                type=temp_item.get("type", "None"),
                text=temp_item.get("text", "None")
            )

        print("current item : ", temp_item)
        object_to_write.write_item()


def start(usr_category):
    base_url = "https://hacker-news.firebaseio.com/v0/"
    user_valid_category = category_getter(usr_category)

    id_list = Item.get_all_ids(user_valid_category, base_url)
    if id_list:
        get_items_and_write_csv(user_valid_category, id_list, base_url)


if __name__ == "__main__":
    try:
        usr_input = str(sys.argv[1])
    except IndexError:
        usr_input = ""
    start(usr_input)
