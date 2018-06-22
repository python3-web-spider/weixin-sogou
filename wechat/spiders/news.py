# -*- coding: utf-8 -*-
import scrapy
from wechat.settings import COOKIES

class NewsSpider(scrapy.Spider):
    name = 'news'
    key_word = 'NBA'
    url = 'http://weixin.sogou.com/weixin?type=2&query={}&page=99'.format(key_word)
    

    def start_requests(self):
        yield scrapy.Request(
            url=self.url,
            cookies=COOKIES,
            callback=self.parse
        )


    def parse(self, response):
        for box in response.css('.txt-box'):
            item = {
                "title": ''.join(box.xpath('./h3//text()').extract()).strip(),
                "content": ''.join(box.xpath('./p//text()').extract()),
                "author": box.css('.s-p a::text').extract_first(),
            }
            yield item
