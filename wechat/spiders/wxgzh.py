# -*- coding: utf-8 -*-
import scrapy
from wechat.settings import COOKIES
from wechat.middlewares import _set_new_ip


class WxgzhSpider(scrapy.Spider):
    name = 'wxgzh'
    key_word = 'NBA'
    url = 'http://weixin.sogou.com/weixin?type=2&query={}&page=78'.format(key_word)

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
        for href in response.css('#sogou_next::attr(href)'):
            yield response.follow(href, callback=self.parse, cookies=COOKIES, meta={'proxy': 'http://localhost:8123'})
            page = int(response.css('#pagebar_container span::text').extract_first())
            if page % 20 == 19:
                _set_new_ip()

    def parse_detail(self, response):
        item = {
            'title': response.css('.rich_media_title::text').extract_first().strip(),
            'content': ''.join(response.css('#js_content p *::text').extract()),
            'date': response.css('#publish_time::text').extract_first(),
            'nickname': response.css('#profileBt a::text').extract_first().strip(),
            'wechat': response.css('#js_profile_qrcode > div > p:nth-child(3) > span::text').extract_first()
        }
        yield item
