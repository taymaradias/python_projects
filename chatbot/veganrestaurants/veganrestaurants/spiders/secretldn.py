# -*- coding: utf-8 -*-
import scrapy
import re

class SecretldnSpider(scrapy.Spider):
    name = 'secretldn'
    allowed_domains = ['secretldn.com']
    start_urls = ['https://secretldn.com/vegan-restaurants-london//']

    def parse(self, response):
        ans = []
        h3 = response.xpath('//div[@class = "entry-content"]//h3')
        name = h3.css('a::text').extract()
        link = h3.xpath('./a/@href').extract()
        loc = h3.xpath('./text()').extract()
        c_l = []
        for lc in loc:
            clean = re.search("[A-Za-z](.*)",lc)
            if clean != None:
                c_l.append(clean.group(0))
        row_data = zip(name[:-1], link[:-1], c_l[:-2])
        for item in row_data:
            scraped_info = {
                'name': item[0],
                'link': item[1],
                'location': item[2],
            }

            yield scraped_info
