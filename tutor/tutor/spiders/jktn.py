from typing import List

import scrapy
from cssselect import Selector


class JktnSpider(scrapy.Spider):
    name = 'jktn'
    allowed_domains = ['https://www.jakartanotebook.com/']
    start_urls = ['https://www.jakartanotebook.com/pc-and-laptop/']

    def parse(self, response):
        detail_products: List[Selector]  = response.css(".product-list-wrapper .product-list")
        for detail in detail_products:

            link = detail.find(attrs={'class': 'product-list__img'}).find('a')

         #   yield {"href": link}
            yield response.follow(href, callback=self.parse_detail())

        yield {"title": response.css("title::text").get()}

    def parse_detail(self, response):
        yield {"title": response.css("title::text").get()}
