from lxml import html
import requests
from pymongo import MongoClient
db = MongoClient('localhost', 27017)['Lenta_news']
collection = db.list_news

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url = 'https://lenta.ru/parts/news/'

response = requests.get(url=url, headers=header).text

root = html.fromstring(response)
links = root.xpath("//*[@id='more']/div")
data_links = []
data_news = []
for link in links:
    link_list = link.xpath("./div[2]/h3/a/@href")
    try:
        data_links.append('https://lenta.ru/' + link_list[0])
    except:
        print('no link')

for link in data_links:
    resp = requests.get(url=link, headers=header).text
    root = html.fromstring(resp)
    try:
        author_news = root.xpath("//span[@itemprop='name']/text()")
    except:
        author_news = 'no author news'

    try:
        name_news = root.xpath("//div[contains(@class,'topic__title')]/text()")
    except:
        name_news = 'no name new'
    try:
        created_time = root.xpath("//time[contains(@class, 'g-date')]/text()")
    except:
        created_time = 'no time'
    data_news.append({
        'sourse_name': author_news,
        'name_news': name_news,
        'link_news': link,
        'created_time': created_time
    })

db.collection.insert_many(
   data_news
)