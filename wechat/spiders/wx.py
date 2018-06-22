# -*- coding: utf-8 -*-
import scrapy


class WxSpider(scrapy.Spider):
    name = 'wx'
    start_urls = ['http://weixin.sogou.com/weixin?type=2&query=NBA&page=9']

    def parse(self, response):
        for href in response.css('h3 a::attr(href)'):
            yield response.follow(href, self.parse_detail)

    def parse_detail(self, response):
        item = {
            'title': response.css('.rich_media_title::text').extract_first().strip(),
            'content': ''.join(response.css('#js_content p *::text').extract()),
            'date': response.css('#publish_time::text').extract_first(),
            'nickname': response.css('#profileBt a::text').extract_first().strip(),
            'wechat': response.css('#js_profile_qrcode > div > p:nth-child(3) > span::text').extract_first()
        }
        yield item

