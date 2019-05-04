# -*- coding: utf-8 -*-
import scrapy
from ..items import WallhavenItem


class WallhavenSpiderSpider(scrapy.Spider):
    name = 'wallhaven_spider'
    allowed_domains = ['alpha.wallhaven.cc']
    start_urls = [
        "https://alpha.wallhaven.cc/search?q=&categories=111&purity=100&atleast=1280x1024&ratios=16x9&topRange=6M&sorting=toplist&order=desc&page=" + str(
            i) for i in range(118)]

    def parse(self, response):
        urls = response.xpath('//*[@id="thumbs"]/section[1]/ul//li//a/@href').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_img)

    def parse_img(self, response):
        try:
            img_utl = "http:" + response.xpath('//*[@id="wallpaper"]/@src').extract()[0]
            img_name = response.xpath('//*[@id="wallpaper"]/@alt').extract()[0]
            item = WallhavenItem()
            item["name"] = img_name
            item["images"] = img_utl
            yield item

        except Exception as e:
            print(e)
