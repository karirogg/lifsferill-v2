import scrapy
import numpy as np
from scrapy.http import Request

class ScrapeSpider(scrapy.Spider):
    # name = 'spiderName'
    # allowed_domains = ['www.projecteuler.net']

    # np.random.seed(0)
    # random_numbers = np.random.uniform(0, 1, size=1000)

    # start_urls = [f'https://projecteuler.net/captcha/show_captcha.php?{x}' for x in random_numbers]

    # def parse(self, response):
    #     item = ImageItem()
    #     if response.status == 200:
    #         rel_img_urls = response.xpath("//img/@src").extract()d
    #         item['image_urls'] = self.url_join(rel_img_urls, response)
    #     return item

    # def url_join(self, rel_img_urls, response):
    #     joined_urls = []
    #     for rel_img_url in rel_img_urls:
    #         joined_urls.append(response.urljoin(rel_img_url))

    #     return joined_urls

    #the name of the spider
    name = 'imagespider'

    #the url of the first page that we will start scraping

    np.random.seed(0)
    random_numbers = np.random.uniform(0, 1, size=1)

    start_urls = ['https://projecteuler.net/captcha/show_captcha.php']

    def parse(self, response):
        self.logger.info('hello this is my first spider')
        quotes = response.css('#captcha_image')
        for quote in quotes:
            self.logger.info(quote)
    
    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)