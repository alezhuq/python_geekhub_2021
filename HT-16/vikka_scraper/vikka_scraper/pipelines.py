# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3

from pathlib import Path
from itemadapter import ItemAdapter
from vikka_scraper.items import VikkaScraperItem


class VikkaScraperPipeline:

    def __init__(self):
        self.conn = sqlite3.connect(Path(Path(__name__).parent / "news.db"))
        self.cur = self.conn.cursor()

    def open_spider(self, spider):
        self.cur.execute(
            f"""CREATE table IF NOT EXISTS news (
                                news_title_text TEXT NOT NULL,
                                date TEXT NOT NULL,
                                full_text TEXT NOT NULL,
                                tags_string TEXT NOT NULL,
                                news_url TEXT NOT NULL
                            )""")

    def process_item(self, item, spider):
        if isinstance(item, VikkaScraperItem):
            with self.conn:
                exist = self.cur.execute("SELECT rowid FROM news WHERE news_title_text = ?", (item["news_title_text"],)).fetchone()
                if not exist:
                    self.cur.execute("""INSERT INTO news (news_title_text, date, full_text, tags_string, news_url)
                    VALUES(?, ?, ?, ?, ?)""",
                                     (
                                         item["news_title_text"],
                                         item["date"],
                                         item["full_text"],
                                         item["tags_string"],
                                         item["news_url"],
                                     ))

        return item

    def close_spider(self, spider):
        pass
