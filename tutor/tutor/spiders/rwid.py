import scrapy
from cssselect import Selector


class RwidSpider(scrapy.Spider):
    name = 'rwid'
    allowed_domains = ['127.0.0.1']
    start_urls = ['http://127.0.0.1:5000/']

    def parse(self, response):
        # yield {"title": response.css("title::text").get()}
        data = {
            "username": "user",
            "password": "user12345"
        }
        return scrapy.FormRequest(
            url="http://127.0.0.1:5000/login",
            formdata=data,
            callback=self.after_login
        )

    def after_login(self, response):
        """
        1 ambil semua data barang di halaman masuk -> akan menuju halaman detail
        2 ambil semua link next -> balik ke after login
        :param response:
        :return:
        # get detail produk
        """
        detail_products: List[Selector] = response.css(".card .card-title a")
        for detail in detail_products:
            href = detail.attrib.get("href")
            yield response.follow(href, callback=self.parse_detail)
        paginations: List[Selector] = response.css(".pagination a.page-link")
        for pagination in paginations:
            href = pagination.attrib.get("href")
            yield response.follow(href,callback=self.after_login)
        yield {"title": response.css("title::text").get()}

    def parse_detail(self, response):
        # yield {"title": response.css("title::text").get()}
        image = response.css(".card-img-top").attrib.get("src")
        title = response.css(".card-title::text").get()
        stock = response.css(".card-stock::text").get()
        description = response.css(".card-text::text").get()
        return {
            "image": image,
            "title" : title,
            "stock" : stock,
            "desc" : description
        }

