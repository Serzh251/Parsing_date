from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import email, password
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from pymongo import MongoClient

db = MongoClient('localhost', 27017)['email_msgs']
collection = db.msg

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=chrome_options)
data_letters = []
msg_links = set()
data_list = []


def parse_messages():
    for url_msg in msg_links:
        driver.get(url_msg)
        time.sleep(1)
        try:
            date = driver.find_element_by_class_name('letter__date').text
            subject = driver.find_element_by_xpath("//h2[@class='thread__subject']").text
            sender_name = driver.find_element_by_class_name('letter-contact').text
            sender_email = driver.find_element_by_class_name('letter-contact').get_attribute('title')
            message_text = driver.find_element_by_class_name('letter__body').text.strip().replace('\n', '.')
            data_list.append({
                'date': date,
                'subject': subject,
                'sender_name': sender_name,
                'sender_email': sender_email,
                'message_text': message_text
            })
        except Exception as ex:
            print(ex)

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

    msg_driver = driver.find_element_by_class_name("dataset__items")
    messages = msg_driver.find_elements_by_tag_name('a')

    while True:
        length = len(msg_links)
        for message in messages:
            link = message.get_attribute('href')
            try:
                if 'e.mail' in link:
                    msg_links.add(link)
            except Exception as ex:
                print(ex)
        try:
            action = ActionChains(driver)
            action.move_to_element(messages[-1])
            action.perform()
            time.sleep(1)
            msg_driver = driver.find_element_by_class_name("dataset__items")
            messages = msg_driver.find_elements_by_tag_name('a')
        except Exception as ex:
            print(ex)
        if length == len(msg_links):
            print(msg_links)
            break
    parse_messages()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


db.collection.insert_many(
   data_list
)