import scrapy


class JktnoteSpider(scrapy.Spider):
    name = 'jktnote'
    start_urls = ['https://www.jakartanotebook.com/electronic']
    def parse(self, response):
        for products in response.css('div.product-list'):
            yield {
                'title': products.css('a.product-list__title::text').get(),
                'price' : products.css('span.product-list__price::text').get(),
                 'url'  :products.css('a.product-list__title').attrib['href'],
                'img'  : products.css('div.product-list__img img::attr(src)').get()
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
