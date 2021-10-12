from itemadapter import ItemAdapter
import scrapy
import json
from pymongo import MongoClient


class HabrPipeline:
    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongobase = client.habr_ru

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item


class HabrPipelineJson:
    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False, indent=4, default=str) + ",\n"
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file = open('result.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()