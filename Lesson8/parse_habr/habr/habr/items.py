import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join


def process_hub(value):
    return value.replace('\n    ', '').replace('\n  ', '')


def process_text(value):
    return value.replace('\r\n', '').replace('\xa0', '')


class HabrParserItem(scrapy.Item):
    _id = scrapy.Field()
    article_author = scrapy.Field(output_processor=TakeFirst())
    article_urls = scrapy.Field(output_processor=TakeFirst())
    article_name = scrapy.Field(output_processor=TakeFirst())
    article_text = scrapy.Field( output_processor=Join(), input_processor=MapCompose(process_text))
    article_image = scrapy.Field()
    article_tag = scrapy.Field()
    article_hub = scrapy.Field(input_processor=MapCompose(process_hub))
    article_add_datetime = scrapy.Field(output_processor=TakeFirst())