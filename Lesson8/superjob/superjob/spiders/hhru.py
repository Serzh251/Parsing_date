import scrapy
from scrapy.http import HtmlResponse
from ..items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://izhevsk.hh.ru/search/vacancy?area=&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.bloko-button::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacansy = response.css(
        	# 'a.bloko-link::attr(href)'
        	'div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)'
    	).extract()
        print(vacansy)
        for link in vacansy:
            yield response.follow(link, callback=self.vacansy_parse)

    def vacansy_parse(self, response: HtmlResponse):
        name = response.css('div.vacancy-title h1.bloko-header-1::text').extract_first()
        # salary = response.css('div.vacancy-title span.bloko-header-2 p.vacancy-salary::text').extract()
        salary_raw = response.xpath('//span[contains(@class,"bloko-header-2")]/text()').getall()
        salary = ''
        for i in salary_raw:
            salary += i.replace(u'\xa0', u'') + ' '
        print(name, salary)
        yield JobparserItem(name=name,salary=salary)