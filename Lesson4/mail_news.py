from lxml import html
import requests
from pymongo import MongoClient
db = MongoClient('localhost', 27017)['mail_news']
collection = db.mail_news

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url = 'https://news.mail.ru/society/'

response = requests.get(url=url, headers=header).text

root = html.fromstring(response)
link_news = root.xpath("//a[contains(@class,'item')]/@href")
data_news = []

for link in link_news:
    resp = requests.get(url=link, headers=header).text
    root = html.fromstring(resp)
    try:
        author_news = root.xpath(".//p/em[1]/text()")
    except:
        author_news = 'no author news'
    try:
        name_news = root.xpath("//h1/text()")
    except:
        name_news = 'no name new'
    try:
        created_time = root.xpath("//time/text()")
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