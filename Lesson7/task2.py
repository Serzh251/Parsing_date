from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'C:\chromedriver.exe')

try:
    driver.get('https://www.onlinetrade.ru/')
    # driver.get('https://www.mvideo.ru/?cityId=CityCZ_975')
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    # driver.execute_script("window.scrollTo(0, 1000)")
    next_button = driver.find_elements_by_xpath("//span[contains(@class, 'swiper-button-next')]")
    # next_button = driver.find_elements_by_xpath("//a[contains(@class, 'c-btn_scroll-horizontal')]")

    for i in range(5):
        next_button[3].click()

    time.sleep(10)
    # берем див новинок целиком. Если тут взять текст, то он есть и забирается весь целиком.
    new_items = driver.find_elements_by_xpath("//div[contains(@aria-live, 'polite')]")[2]
    # ищем в нем товары. отсюда уже текста нет
    items = new_items.find_elements_by_class_name("swiper-slide")
    # перебираем список товаров
    for item in items:
        # название товара
        good_name = item.find_element_by_class_name('indexGoods__item__manageTop').find_element_by_tag_name('a')
        print(good_name)
        # цена товара
        good_price = item.find_element_by_class_name('indexGoods__item__dataCover').find_element_by_class_name('indexGoods__item__price').find_element_by_tag_name('span')
        print(good_price.text, 'end')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
