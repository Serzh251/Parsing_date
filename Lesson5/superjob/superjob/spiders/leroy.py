import scrapy
from scrapy.http import HtmlResponse
from ..items import LeroyparserItem
from scrapy.loader import ItemLoader


class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, mark, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://arkhangelsk.leroymerlin.ru/search/?q={mark}']

    def parse(self, response: HtmlResponse):
        ads_links = response.xpath('//div[@data-qa-product]/a')
        for link in ads_links:
            yield response.follow(link, callback=self.parse_item)

    def parse_item(self, response):
        item_loaded = ItemLoader(item=LeroyparserItem(), response=response)
        item_loaded.add_xpath('file_name', '//h1/text()'),
        item_loaded.add_xpath('file_urls', '//*[@slot="pictures"]/source[1]/@srcset')
        item_loaded.add_xpath('price', '//span[@slot="price"]/text()')
        yield item_loaded.load_item()