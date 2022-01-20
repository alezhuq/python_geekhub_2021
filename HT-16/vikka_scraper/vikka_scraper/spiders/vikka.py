# Переробити попереднє домашнє завдання: зберігати результати в базу, використовуючи pipelines.
import scrapy

from bs4 import BeautifulSoup
from vikka_scraper.items import VikkaScraperItem

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
            try:
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
            except AttributeError:
                return None

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

        name_of_file = f"{response.meta['year']}{response.meta['month']}{response.meta['day']}"

        item = VikkaScraperItem()

        item["date"] = name_of_file
        item["news_title_text"] = response.meta["news_title_text"]
        item["full_text"] = full_text
        item["tags_string"] = tags_string
        item["news_url"] = response.meta["news_url"]

        yield item
