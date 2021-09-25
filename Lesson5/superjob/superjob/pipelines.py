from os.path import splitext
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import scrapy
from pymongo import MongoClient


class SuperjobPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacansy_280

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        # print(item['salary'])

        return item


class JobparserPipeline(object):
    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongobase = client.vacansy_288

    def process_item(self, item, spider):
        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        print(item['salary'])

        return item


class DataBasePipeline(object):
    def __init__(self):
        client = MongoClient('localhost',27017)
        self.mongo_base = client.leroy_photo

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item


class LeroyPhotosPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'filename': item.get('file_name')}) for x in item.get(self.files_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        url = request.url
        media_ext = splitext(url)[1]
        return f'{request.meta["filename"]}\{request.meta["filename"]}{media_ext}'
        # print('<<<<<<<-------------->>>>>>>>', request)
        # return f'photo\\{request.meta["filename"]}{media_ext}'
        # return f'item["file_name"]\{request.meta["file_name"]}{media_ext}'
        return f'{request.meta["filename"]}\{request.meta["filename"]}{media_ext}'
