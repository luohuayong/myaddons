# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class GuaziSaleSpider(scrapy.Spider):
    name = 'guazi_sale'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/wh/buy/o3/#bread']

    cookies = {'antipas': '57Z575218968bL6r20iIe1E1B2'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    def start_requests(self):
        url = 'https://www.guazi.com/wh/buy/o3/#bread'
        yield Request(url=url, cookies=self.cookies, headers=self.headers, callback=self.parse)

    def parse(self, response):
        for item in response.xpath("//ul[@class='carlist clearfix js-top']//a/@href"):
            next_page = response.urljoin(item.extract())
            yield Request(url=next_page, cookies=self.cookies,
                          headers=self.headers, callback=self.parse_detail)

    def parse_detail(self, response):
        yield {
            'title': response.xpath("//div[@class='titlebox']/p/text()").extract_first(),
            'url': response.url,
            'shangpai_date': response.xpath("//li[@class='one']/span/text()").extract_first(),
            'xingshi': response.xpath("//li[@class='two']/span/text()").extract_first(),
            'address': response.xpath("//li[@class='three']/span/text()").extract_first(),
            'price': response.xpath("//span[@class='pricestype']/text()").extract_first(),
            'price_new': response.xpath("//span[@class='newcarprice']/text()").extract_first(),
        }
