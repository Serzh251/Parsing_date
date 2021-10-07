from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from pymongo import MongoClient

db = MongoClient('localhost', 27017)['Mvideo']
collection = db.hits

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=chrome_options)
data = []
try:
    driver.get('https://www.mvideo.ru/')
    # закрытие всплывающего окна
    close = driver.find_element_by_xpath("//*[contains(@class, 'modal-layout__close')]")
    close.click()
    hits = driver.find_element_by_xpath("//mvid-product-cards-group")
    action = ActionChains(driver)
    action.move_to_element(hits)
    action.perform()
    names = driver.find_elements_by_xpath('//*[contains(@class, "product-mini-card__name")]')
    price = driver.find_elements_by_xpath('//*[contains(@class, "product-mini-card__price")]')
    for i in range(0, len(names)):
        data.append({
            'name': names[i].text,
            'price': price[i].text.split('\n')[0],  # в скидки не верю)
            'link': names[i].find_element_by_class_name('title').find_element_by_tag_name('a').get_attribute('href')
        })

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


db.collection.insert_many(
   data
)