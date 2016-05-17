# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from bootstrap.items import BootstrapItem
class BootstrapitemSpider(scrapy.Spider):
    name = "bootstrap"
    start_urls = (
        'http://expo.bootcss.com',
    )
    output = open('data', 'w')
    def parse(self, response):
        container = response.xpath('//main').css('.container')
        rowDivs = container.xpath('div').xpath('div')
        for card in rowDivs:
            title = card.xpath('article').xpath('h2')
            item = BootstrapItem()
            titles = title.xpath('a//text()').extract()
            imageURLs=card.xpath('article').xpath('div').xpath('a').xpath('img/@src').extract()
            siteURLs = card.xpath('article').xpath('div').xpath('p').xpath('a/@href').extract()
            item['title']=titles[0]
            item['image_urls']=[imageURLs[0].replace('!thumb','')]
            item['siteURL']=siteURLs[0]
            self.output.write(str(item)+'\n')
            print '\nitem :'+str(item)
            yield item
        nextPageView = container.css('.pagination').css('.older-posts')
        if (nextPageView == []):
            self.output.close()
            print '\n\nScrapy finish'
        else:
            nextURL = self.start_urls[0] + nextPageView.xpath('@href').extract()[0]
            yield Request(url=nextURL, meta={'item':item},callback=self.parse)
