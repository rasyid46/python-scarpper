import scrapy


class JktnoteSpider(scrapy.Spider):
    name = 'jktnote'

    start_urls = ['http://https://www.jakartanotebook.com/electronic']

    def parse(self, response):
        for products in response.css('div.div.product-list'):
            price = products.css('span.product-list__price::text').get()
            yield {
                'price':price
            }
        pass
