from os.path import splitext
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import scrapy
from pymongo import MongoClient
import csv

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


class CSVPipeline():
    def __init__(self):
        self.file = f'database.csv'
        with open(self.file, 'r', newline='', encoding='UTF-8') as csv_file:
            self.tmp_data = csv.DictReader(csv_file).fieldnames

        self.csv_file = open(self.file, 'a', newline='', encoding='UTF-8')

    def __del__(self):
        self.csv_file.close()

    def process_item(self, item, spider):
        columns = item.fields.keys()

        data = csv.DictWriter(self.csv_file, columns)
        if not self.tmp_data:
            data.writeheader()
            self.tmp_data = True
        data.writerow(item)
        return item
