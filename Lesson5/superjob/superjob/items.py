import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose


class SuperjobItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()


class JobparserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()


def process_file_name(value):
    return value.replace('/', '_')


def process_price(value):
    try:
        return int(value.replace(' ', ''))
    except:
        return value


class LeroyparserItem(scrapy.Item):
    _id = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(process_price),
                         output_processor=TakeFirst()
                         )
    file_urls = scrapy.Field()
    file_name = scrapy.Field(input_processor=MapCompose(process_file_name),
                             output_processor=TakeFirst()
                             )


