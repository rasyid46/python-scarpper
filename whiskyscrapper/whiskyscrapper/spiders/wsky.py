import scrapy


class WskySpider(scrapy.Spider):
    name = 'wsky'
    allowed_domains = ['www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']
    start_urls = ['http://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock/']

    def parse(self, response):
        pass
