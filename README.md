# weixin_sogou
## 使用微信二维码登陆搜狗，搜索关键词显示100页

登陆后修改wechat/settings.py, 替换COOKIES为你的， 格式如下。

```
COOKIES = {
    'ppmdig': '*',
    'SUV': '*'
}
```
可自己修改关键词
`wechat/spider/wxgzh.py`

```
key_word = 'NBA'
```

## 使用代理
反爬使用tor代理或ADSL动态拨号代理。如果使用tor，安装tor与polipo或privoxy，这里选择polipo，修改相关的配置。

使用tor代理与polipo，wxgzh.py文件部分如下

```python
for href in response.css('#sogou_next::attr(href)'):
    yield response.follow(href, callback=self.parse, cookies=COOKIES, meta={'proxy': 'http://localhost:8123'})
    # 切换tor代理 ip
    page = int(response.css('#pagebar_container span::text').extract_first())
    if page % 20 == 19: # 20个下一页换一次 ip
       _set_new_ip()
```

不使用代理则修改wxgzh.py

```
for href in response.css('#sogou_next::attr(href)'):
    yield response.follow(href, callback=self.parse, cookies=COOKIES)
```
