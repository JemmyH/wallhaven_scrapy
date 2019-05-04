# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings


class WallhavenPipeline(object):
    def __init__(self):
        self.file_path = open(get_project_settings().get("LOCAL_PATH"), "w")

    def open_spider(self, spider):
        print("start...")

    def process_item(self, item, spider):
        self.file_path.write("{},{}\n".format(item["name"], item["images"]))
        return item

    def close_spider(self, spider):
        self.file_path.close()
        print("finished...")
