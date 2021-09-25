import scrapy
from scrapy.loader.processors import TakeFirst

class SuperjobItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()


class JobparserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()


class LeroyparserItem(scrapy.Item):
    _id = scrapy.Field()
    price = scrapy.Field()
    file_urls = scrapy.Field()
    file = scrapy.Field()
    file_name = scrapy.Field(
        output_processor=TakeFirst()
    )
