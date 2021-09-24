from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import email, password
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\chromedriver.exe')
data_letters = []

try:
    driver.get('https://mail.ru/')
    emal_input = driver.find_element_by_name("login")
    emal_input.clear()
    emal_input.send_keys(email)
    time.sleep(1)
    enter_pasword_btn = driver.find_element_by_xpath("//button[@data-testid='enter-password']")
    enter_pasword_btn.send_keys(Keys.ENTER)
    time.sleep(1)
    input_password = driver.find_element_by_xpath("//*[@type='password']")
    input_password.clear()
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)
    time.sleep(10)
    # driver.execute_script("window.scrollTo(0, 1000)")
    # скролл сообщений не работает, хотя эти методы работают например в task2
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    msg_links = driver.find_elements_by_xpath("//a[contains(@class, 'llc')]/@href")
    print(msg_links)
    for link in msg_links:
        driver.get(link)
        time.sleep(1)
        print(link)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

