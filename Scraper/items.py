# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyItem(scrapy.Item):
    isActor = scrapy.Field()
    isFilm = scrapy.Field()
    year = scrapy.Field()
    url = scrapy.Field()

class Film(ScrapyItem):
    # define the fields for your item here like:
    filmName = scrapy.Field()
    filmValue = scrapy.Field()
    actors = scrapy.Field()
    starrings = scrapy.Field()

class Actor(ScrapyItem):
    # define the fields for your item here like:
    actorName = scrapy.Field()
    films = scrapy.Field()
    castings = scrapy.Field()
