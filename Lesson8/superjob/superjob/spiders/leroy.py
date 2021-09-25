import scrapy
from scrapy.http import HtmlResponse
from ..items import LeroyparserItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from urllib.parse import urljoin
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, mark):
        self.start_urls = [f'https://arkhangelsk.leroymerlin.ru/search/?q={mark}']
    # start_urls = [f'https://arkhangelsk.leroymerlin.ru/search/?q=насос']

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths="//a[contains(@class, 's15wh9uj_plp')]/@href")),
    #     Rule(LinkExtractor(restrict_xpaths='//div[contains(@class, "phytpj4_plp largeCard")]/a/@href'), callback='parse_item')
    # )
    def parse(self, response: HtmlResponse):
        ads_links = response.xpath('//div[contains(@class, "phytpj4_plp largeCard")]/a/@href').extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_item)

    # def parse_ads(self, response):
    #     name = response.xpath ('//h1[@class="header-2"]/text()').extract()
    #     photos = response.xpath('//*[@slot="pictures"]/source[1]/@srcset').extract()
    #     price = response.xpath('//span[@slot="price"]/text()').extract()
    #
    #     yield LeroyparserItem(name=name, photos=photos,price=price)
    #     # print(name, photos, price)


    def parse_item(self, response):
        item_loaded = ItemLoader(item=LeroyparserItem(), response=response)
        item_loaded.add_xpath('file_name', '//h1[@class="header-2"]/text()',
                    MapCompose(lambda i: i.replace('/', ','))),
        item_loaded.add_xpath('file_urls', '//*[@slot="pictures"]/source[1]/@srcset',
                    MapCompose(lambda i: urljoin(response.url, i)))
        return item_loaded.load_item()