from typing import List

import scrapy
from cssselect import Selector


class JktnSpider(scrapy.Spider):
    name = 'jktn'
    allowed_domains = ['https://www.jakartanotebook.com/']
    start_urls = ['https://www.jakartanotebook.com/pc-and-laptop/']

    def parse(self, response):
        detail_products: List[Selector]  = response.css(".product-list__header")
        for product in detail_products:
            href = product.attrib.get("href")
            yield {"title": response.css("title::text").get(),"href":href}

