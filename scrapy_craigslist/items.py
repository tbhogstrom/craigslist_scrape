# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigslistCar(scrapy.Item):
    link = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    modelraw = scrapy.Field()
    presDims =scrapy.Field()
    detailCorp = scrapy.Field()