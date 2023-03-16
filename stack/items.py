# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Field, Item


class StackItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    title = Field()

class VNExpressItem(Item):
    url = Field()
    title = Field()
    description = Field()
