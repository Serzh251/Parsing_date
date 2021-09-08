from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
url = (f'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%90%D1%80%D1%85%D0%B0%D0%BD%D0%B3%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B5,_%D0%90%D1%80%D1%85%D0%B0%D0%BD%D0%B3%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C')

response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response, 'lxml')
lst =soup.find(id='SensorsListTitle')
temp = lst.findAll(class_='t_0')
for t in temp:
    print(t.text)
print(temp)