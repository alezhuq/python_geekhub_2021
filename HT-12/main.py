# 1. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
#    цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу.
#    Результати зберегти в репозиторії.
#    Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL).
#    Хто захардкодить пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)
import sqlite3
import time
import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path


def create_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
        return con
    except sqlite3.Error as e:
        print(e)

    return con


def info_getter(soup, web_url, con, cur):
    page_quotes = soup.find_all("div", {'class': 'quote'})
    for quote in page_quotes:
        text_quote = quote.find("span", {"class": "text"}).getText()

        author = quote.find("small", {"class": "author"}).getText()

        span_author_url = quote.findChildren("span", recursive=False)

        # find the authors info location
        author_url = None
        for i in span_author_url:
            if i.find("a"):
                author_url = i.find("a").attrs["href"]
                break

        try:
            author_request = requests.get(web_url + author_url)
            author_request.raise_for_status()
            time.sleep(0.1)

        except:
            print("can't open the web page1")
            exit(1)

        temp_soup = BeautifulSoup(author_request.text, "lxml")

        author_info = temp_soup.find("div", {"class": "author-description"}).text
        author_born_date = temp_soup.find("span", {"class": "author-born-date"}).text
        author_born_location = temp_soup.find("span", {"class": "author-born-location"}).text
        all_tags_html = quote.find("meta", {"class": "keywords"})
        all_tags = all_tags_html.attrs["content"]

        with open(Path(Path("__file__").parent / "out.csv"), "a") as out:
            writer = csv.writer(out)
            writer.writerow(
                [text_quote, author, author_info[9:-9], author_born_date, author_born_location[3:], all_tags])
        print([text_quote, author, author_info[9:-9], author_born_date, author_born_location[3:], all_tags])
        exist = cur.execute("SELECT rowid FROM quotes WHERE quote = ?", (text_quote,)).fetchone()
        if not exist:
            with con:
                cur.execute("""INSERT INTO quotes(quote, author, author_info, author_born_date, author_born_location, tags)
                            VALUES (?, ?, ?, ?, ?, ?)""",
                            (text_quote, author, author_info[9:-9], author_born_date, author_born_location[3:], all_tags,))


    return "success"


def get_all_pages_info(con, cur):
    web_url = "http://quotes.toscrape.com/"

    try:
        request = requests.get(web_url)
        request.raise_for_status()
        time.sleep(0.5)
    except:
        print("can't open the web page2")
        return

    soup = BeautifulSoup(request.text, "lxml")
    info_getter(soup, web_url, con, cur)

    is_next_link = soup.find("li", {"class": "next"})

    while is_next_link:
        nextlink = is_next_link.find("a").attrs['href']
        try:
            request = requests.get(web_url + nextlink)
            request.raise_for_status()
            time.sleep(0.1)
        except:
            print("can't open the web page")
            exit(1)

        soup = BeautifulSoup(request.text, "lxml")
        result = info_getter(soup, web_url, con, cur)
        if not result:
            print("something gone wrong")
        is_next_link = soup.find("li", {"class": "next"})
        print(nextlink)

    if result:
        print(result)


def main():
    with open(Path(Path("__file__").parent / "out.csv"), "w") as out:
        writer = csv.writer(out)
        writer.writerow(["quote", "author", "author_info", "author_born_date", "author_born_location", "tags"])

    create_quotes_table = """ CREATE TABLE IF NOT EXISTS quotes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                quote TEXT NOT NULL,
                                author TEXT NOT NULL,
                                author_info TEXT NOT NULL,
                                author_born_date TEXT NOT NULL,
                                author_born_location TEXT NOT NULL,
                                tags TEXT NOT NULL
                                ); """
    con = create_connection(Path("__file__").parent / "quotes.db")
    cur = con.cursor()
    with con:
        cur.execute(create_quotes_table)

    get_all_pages_info(con, cur)


if __name__ == "__main__":
    main()
