from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
import json

search_text = input('введите то что вы ищете: ')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
url = (f'https://www.superjob.ru/vacancy/search/?keywords={search_text}')

response = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
data = []

items = soup.find_all('div', class_='f-test-search-result-item')

for i in items:
    try:
        salary = i.find('span', class_='f-test-text-company-item-salary').text
    except:
        salary = 'no data salary'
    try:
        name = i.find('a', class_='icMQ_').text
    except:
        name = 'no data name'
    try:
        link = 'https://www.superjob.ru/' + i.find('a').get("href")
    except:
        link = 'no data link'
    data.append({
        'link': link,
        'name': name,
        'salary': salary
    })

pd.DataFrame(data).to_csv('vacancies.csv', index=False, encoding='utf-8')

with open('vacancies_list.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)