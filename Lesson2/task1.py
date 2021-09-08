from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
import json

search_text = input('введите то что вы ищете: ')

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
url = (f'https://www.superjob.ru/vacancy/search/?keywords={search_text}')
# url = (f'https://hh.ru/search/vacancy?clusters=true&area=113&ored_clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=python')

response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
data = []
app = soup.find(id='app')
item = app.findAll(class_='f-test-search-result-item')
for i in item:
    link = soup.find("a", {"class": "_6AfZ9"})
    salary = soup.find(class_='f-test-text-company-item-salary')
    salary = salary.text
    data.append({
        'link': 'https://www.superjob.ru/' + link['href'],
        'name': link.text,
        'salary': salary
    })

pd.DataFrame(data).to_csv('vacancies.csv', index=False, encoding='utf-8')
