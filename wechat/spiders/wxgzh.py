# -*- coding: utf-8 -*-
import scrapy
from wechat.settings import COOKIES


class WxgzhSpider(scrapy.Spider):
    name = 'wxgzh'
    key_word = 'NBA'
    url = 'http://weixin.sogou.com/weixin?type=2&query={}&page=99'.format(key_word)

    def start_requests(self):
        yield scrapy.Request(
            url=self.url,
            cookies=COOKIES,
            callback=self.parse,
        )
    
    def parse(self, response):
        for href in response.css('h3 a::attr(href)'):
            yield response.follow(href, self.parse_detail)

        # follow pagination links
        #"""
        next_page = response.css('#sogou_next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, cookies=COOKIES)
        #"""

    def parse_detail(self, response):
        item = {
            'title': response.css('.rich_media_title::text').extract_first().strip(),
            'content': ''.join(response.css('#js_content p *::text').extract()),
            'date': response.css('#publish_time::text').extract_first(),
            'nickname': response.css('#profileBt a::text').extract_first().strip(),
            'wechat': response.css('#js_profile_qrcode > div > p:nth-child(3) > span::text').extract_first()
        }
        yield item
