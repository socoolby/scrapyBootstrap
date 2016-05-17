# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class BootstrapItem(scrapy.Item):
    title = scrapy.Field()
    siteURL = scrapy.Field()
    imagePath = scrapy.Field()
    image_urls = scrapy.Field()

    def __repr__(self):
        return 'title:{title} image_urls:{image_urls} siteURL:{siteURL}'.format(title=self['title'],
                                                                                image_urls=self['image_urls'],
                                                                                siteURL=self['siteURL'])
