# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request
from urllib.parse import urlencode
from toutiao.items import ImageItem
import json

class ImagesSpider(Spider):
    name = 'toutiao'
    allowed_domains = ['toutiao.com']
    start_urls = ['http://www.toutiao.com/']

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('data'):
            item = ImageItem()
            if image.get('cell_type') is not None:
                continue
            item['title'] = image.get('title')
            pic=image.get('image_list')
            for pi in pic:
                picurl='https:'+pi.get('url')+'.jpg'
            item['url']=picurl
            yield item

    
    def start_requests(self):
        data = {
            'format':'json',
            'keyword':'街拍',
            'autoload':'true',
            'count':'20',
            'cur_tab':'1',
            'from':'search_tab'
        }
        base_url = 'http://www.toutiao.com/search_content/?'
        group=([x*20 for x in range(1,20+1)])
        group_new=[str(x) for x in group]
        for page in group_new:
            data['offset'] = page
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)