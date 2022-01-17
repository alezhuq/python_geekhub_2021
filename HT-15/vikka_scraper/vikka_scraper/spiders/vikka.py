# Легенда:
#     - Клієнт для свого проєкта замовив у вас бота, який буде створювати файл з новинами про події у місті
#     за певний день. Клієнт має певні побажання щодо формату файлу, даних у ньому та технологіях,
#     які будуть використовуватися (клієнт планує сам підтримувати свій проєкт, але він знає лише Python
#     та трохи розбирається у Scrapy і BeautifulSoup)
# Завдання:
#     Напишіть скрейпер для сайту "vikka.ua", який буде приймати від користувача дату,
#     збирати і зберігати інформацію про новини за вказаний день.
# Особливості реалізації:
#     - використовувати лише Scrapy, BeautifulSoup (опціонально), lxml (опціонально) та вбудовані модулі Python
#     - дані повинні зберігатися у csv файл з датою в якості назви у форматі "рік_місяць_число.csv"
#     (напр. 2022_01_13.csv)
#     - дані, які потрібно зберігати (саме в такому порядку вони мають бути у файлі):
#         1. Заголовок новини
#         2. Текст новини у форматі рядка без HTML тегів та у вигляді суцільного тексту
#         (Добре: "Hello world" Погано: "<p>Hello</p><p>world</p>")
#         3. Теги у форматі рядка, де всі теги записані з решіткою через кому (#назва_тегу, #назва_тегу, ...)
#         4. URL новини
#     - збереження даних у файл може відбуватися за бажанням або в самому спайдері, або через Pipelines
#     (буде плюсом в карму)
#     - код повинен бути написаний з дотриманням вимог PEP8 (іменування змінних, функцій, класів, порядок імпортів,
#     відступи, коментарі, документація і т.д.)
#     - клієнт не повинен здогадуватися, що у вас в голові - додайте якісь підказки там, де це необхідно
#     - клієнт може випадково ввести некорректні дані, пам'ятайте про це
#     - якщо клієнту доведеться відправляти вам бота на доопрацювання багато разів,
#     або не всі його вимоги будуть виконані - він знайде іншого виконавця, а з вами договір буде розірваний.
#     У нього в команді немає тестувальників, тому перед відправкою завдання - впевніться,
#     що все працює і відповідає ТЗ.
#     - не забудьте про requirements.txt
#     - клієнт буде запускати бота через термінал командою "scrapy crawl назва_скрейпера"
import csv
import scrapy

from bs4 import BeautifulSoup
from pathlib import Path
import datetime as dt


class VikkaSpider(scrapy.Spider):
    name = 'vikka'
    allowed_domains = ['vikka.ua']
    start_urls = ['http://vikka.ua//']

    def start_requests(self):
        # function that asks for date and yields (formatted) url on that date or None
        date_format = "%d %m %Y"

        # check if date input is correct
        try:
            input_date = dt.datetime.strptime(
                input("input your date in the following format : dd mm YYYY :"),
                "%d %m %Y"
            )
            day, month, year = dt.datetime.strftime(input_date, date_format).split(sep=" ")
            now = dt.datetime.now()
            if input_date > now:
                print("future")
                return None
        except TypeError:
            print("type!!")
            return None
        except ValueError:
            print("can't read your date")
            return None

        # url of web page to parse
        final_url = f"{VikkaSpider.start_urls[0]}/{year}/{month}/{day}"

        yield scrapy.Request(
            url=final_url,
            callback=self.parse_news,
            meta={
                "year": year,
                "month": month,
                "day": day
            }
        )

    def parse_news(self, response, **kwargs):
        soup = BeautifulSoup(response.text, "lxml")

        container_with_news = soup.select_one("#primary > ul")

        # gathering info : title and url :
        for news in container_with_news.find_all("li"):
            title = news.select_one(".title-cat-post")
            temp_url = title.a.get("href")

            # going inside each url to gather text of news :
            yield scrapy.Request(
                url=temp_url,
                callback=self.parse_news_text_and_write,
                meta={
                    "year": response.meta["year"],
                    "month": response.meta["month"],
                    "day": response.meta["day"],
                    "news_title_text": title.text,
                    "news_url": temp_url
                }
            )

        #checking if ther is pagination
        next_page = soup.select_one("#primary > nav")

        if next_page:
            link = next_page.select_one(".next.page-numbers").get("href")
            print("-"*40)
            print(link)
            print("-"*40)
            yield scrapy.Request(
                url=link,
                callback=self.parse_news,
                meta={
                    "year": response.meta["year"],
                    "month": response.meta["month"],
                    "day": response.meta["day"],
                }
            )

    def parse_news_text_and_write(self, response, **kwargs):

        soup = BeautifulSoup(response.text, "lxml")
        container_with_pieces_of_text = soup.select_one(".entry-content.-margin-b")

        # collecting text
        full_text = str()
        for p1_container in container_with_pieces_of_text.find_all("p"):
            piece_of_text = p1_container.text
            full_text += " "
            full_text += piece_of_text

        # collecting and formating tags
        tags_string = str()
        for container_with_tag in soup.find_all("a", class_="post-tag"):
            tags_string += "#" + container_with_tag.text + " "

        name_of_file = f"{response.meta['year']}_{response.meta['month']}_{response.meta['day']}.csv"

        list_to_write = [response.meta["news_title_text"], full_text, tags_string, response.meta["news_url"]]
        # opening file and adding info
        with open(Path(Path("__name__").parent.parent.parent / name_of_file), "a") as file:
            writer = csv.writer(file)
            writer.writerow(list_to_write)
