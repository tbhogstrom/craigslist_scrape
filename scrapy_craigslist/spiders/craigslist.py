# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider, Request
from scrapy_craigslist.items import CraigslistCar
#from scrapy_craigslist.pipelines import ExportItem
import json

class CraigslistSpider(Spider):
    name = 'craigslist'

    start_urls = ['https://portland.craigslist.org/search/cto']

    BASE_URL = 'https://portland.craigslist.org'

    def parse(self, response):
        links = response.xpath('//a[@class="result-title hdrlnk"]/@href').extract()
        for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)
            
    def parse_attr(self, response):
        item = CraigslistCar()
        item["link"] = response.url
        item["price"] = response.css("span.price::text").extract_first() 
        item["date"] = response.css("time.timeago::text").extract_first()
        item["title"] = response.css("span#titletextonly::text").extract_first()
        item["modelraw"] = response.xpath("//section/div/p/span/b/text()").extract_first()
        item["presDims"] = response.xpath("//section/div/p/span/text()").extract()
        detName = response.xpath("//section/div/p/span/text()").extract()
        ##Take colon and blank space out of detail Detname
        details = [s.replace(': ', '') for s in detName]
        rawDet = response.xpath("//section/div/p/span/b/text()").extract()
        del rawDet[0]
        item["detailCorp"] = rawDet
        ##Dictionary of car detaiil feilds, formatted like
        dims = dict(zip(details, rawDet))
        print(dims)
        #item["detailCorp"] = response.xpath("//section/div/p/span/b/text()").extract()
        yield item 
      


        # Follows subsequent listing pages
        # next_page = response.xpath('//a[contains(@class, "button next")]/@href').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield Request(next_page, callback=self.parse)
