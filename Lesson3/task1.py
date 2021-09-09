import re

from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
import json
from pymongo import MongoClient
db = MongoClient('localhost', 27017)['GB']
# db = client['vacancies_database']
collection = db.list_vacancies
# search_text = input('введите то что вы ищете: ')

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
# url = (f'https://www.superjob.ru/vacancy/search/?keywords={search_text}')
url = (f'https://www.superjob.ru/vacancy/search/?keywords=водитель')

response = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
data = []

items = soup.find_all('div', class_='f-test-search-result-item')

for i in items:
    try:
        salary_str = i.find('span', class_='f-test-text-company-item-salary').text
        salary_lst = re.findall(r'\d+', salary_str)
        salary_temp = ''
        for item in salary_lst:
            salary_temp += item
        # nums = [int(i) for i in nums]
        salary = int(salary_temp)
        # print(salary_str)
        # print(salary_lst)
        # print(salary)
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

db.collection.insert_many(
   data
)


def find_salary(number):
    cursor = db.collection.find({'salary': {"$gt": number}}).sort('salary')
    for item in cursor:
        print(item)


def add_new_vacancy():
    for name in data:
        data_name = name.get('name')
        db.collection.update_one({'name': data_name}, {'$set':{'name': data_name}}, upsert=True)


add_new_vacancy()
find_salary(100000)