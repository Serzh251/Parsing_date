from lxml import html
import requests
from pymongo import MongoClient
db = MongoClient('localhost', 27017)['yandex_news']
collection = db.yandex_news

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url = 'https://yandex.ru/news'

response = requests.get(url=url, headers=header).text

root = html.fromstring(response)
link_news = root.xpath("//*[contains(@class, 'mg-card')]/a/@href")
data_news = []

for link in link_news:
    resp = requests.get(url=link, headers=header).text
    root = html.fromstring(resp)

    try:
        author_news = root.xpath("//*[@id='b7UAq-page']/div/div[2]/div/div[1]/article/div[1]/a/span[2]")
        print(author_news)
    except:
        author_news = 'no author news'

    try:
        name_news = root.xpath("//h1[contains(@class, 'mg-story__title')]")
        print(name_news)
    except:
        name_news = 'no name new'

    data_news.append({
        'sourse_name': author_news,
        'name_news': name_news,
        'link_news': link,
    })

db.collection.insert_many(
    data_news
)