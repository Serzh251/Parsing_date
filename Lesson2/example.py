from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
import json


headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
url = (f'https://www.superjob.ru/vacancy/search/?keywords=водитель')

response = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
# data = []
# app = soup.find(id='app')
# item = app.findAll(class_='f-test-search-result-item')
# for i in item:
#     link = soup.find("a", {"class": "_6AfZ9"})
#     salary = soup.find(class_='f-test-text-company-item-salary')
#     salary = salary.text
#     data.append({
#         'link': 'https://www.superjob.ru/' + link['href'],
#         'name': link.text,
#         'salary': salary
#     })
items = soup.find_all('div', class_='f-test-search-result-item')
for i in items:
    try:
        print(i.find('span', class_='f-test-text-company-item-salary').text)
        print(i.find('a', class_='icMQ_').text)
        print(i.find('a').get("href"))
    except:
        print('no data')
    print('------')