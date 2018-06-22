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
### 反爬使用tor代理或ADSL动态拨号代理。如果使用tor，就注释掉settings.py里的DOWNLOADER_MIDDLEWARES，并安装tor与polipo或privoxy，这里选择polipo，修改相关的配置。
