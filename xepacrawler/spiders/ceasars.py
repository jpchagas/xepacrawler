import scrapy


class CeasarsSpider(scrapy.Spider):
    name = 'ceasars'
    allowed_domains = ['ceasa.rs.gov.br']
    start_urls = ['http://ceasa.rs.gov.br/']

    def parse(self, response):
        pass
