# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class VikkaScraperItem(Item):
    date = Field()
    news_title_text = Field()
    full_text = Field()
    tags_string = Field()
    news_url = Field()
    pass
