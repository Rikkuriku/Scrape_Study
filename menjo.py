from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import numpy as np
import requests


def taiki(driver, X_path, keys):
    try:
        c_box = driver.find_element(by=By.XPATH, value=X_path)
        if keys == None:
            c_box.click()
        else:
            c_box.send_keys(keys)
            c_box.submit()
        sleep(1)
    except:
        taiki(X_path, keys)


def send_message():
  headers = {
      'Authorization': 'XOm1PIk4UMT3dPFIrc9NaA192QUdgb3sGL3vJh6FCP7',
  }

  files = {
      'message': (None, 'TEXT'),
  }

  requests.post('https://notify-api.line.me/api/notify', headers=headers, files=files)


driver = webdriver.Chrome("D:\downloadapps\chromedriver\chromedriver_win32\chromedriver")
target_url = "https://slsi.skr.u-ryukyu.ac.jp/gksien/"
driver.get(target_url)
sleep(3)
X_path = '//*[@id="wp-block-search__input-1"]'
search = '授業料免除'
taiki(driver, X_path, search)
X_path = '//*[@id="gtranslate_selector"]/option[3]'
taiki(driver, X_path, None)
X_path = '//*[@id="content"]/ul/child::li/a'
tmp = driver.find_elements(by=By.XPATH, value=X_path)

MESSAGE = ''
for i in tmp:
    MESSAGE += i.text + "\n" + i.get_attribute('href') + "\n"


def main():
    send_line_notify(MESSAGE)

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = '45CxY5aSxqO4B3lqD1C2XZXP8uYo6nbQ3U8QhlKNeA2'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()

send_line_notify(MESSAGE)
