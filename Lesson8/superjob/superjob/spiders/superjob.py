import scrapy
from scrapy.http import HtmlResponse
from ..items import SuperjobItem


class SuperjobSpider(scrapy.Spider):
    name = 'superjob'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://russia.superjob.ru/vacancy/search/?keywords=python']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.f-test-button-dalshe::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacansy = response.css(
            'div._3zucV div.f-test-search-result-item div._1h3Zg a.icMQ_::attr(href)'
        ).extract()

        for link in vacansy:
            yield response.follow(link, callback=self.vacansy_parse)

    def vacansy_parse(self, response: HtmlResponse):
        name = response.css('h1._1h3Zg::text').extract_first()

        salary_raw = response.xpath('//span[contains(@class,"f-test-text-company-item-salary")]/span/span/text()').getall()
        salary = ''
        for i in salary_raw:
            salary += i.replace(u'\xa0', u'') + ' '
            if i == 'месяц':
                break

        # print(name, salary)
        yield SuperjobItem(name=name, salary=salary)