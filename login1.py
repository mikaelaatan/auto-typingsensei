from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import random
import pickle


# browser = webdriver.Chrome()
# browser.get(('http://typingsensei.com/play'))

options = webdriver.ChromeOptions()
# capability = DesiredCapabilities.CHROME
# capability["pageLoadStrategy"] = "normal"
options.add_argument('user-data-dir=selenium0')
options.add_argument('ignore-certificate-errors')
options.add_experimental_option("detach", True)
options.add_argument("enable-javascript")
options.add_argument("allow-scripts")
options.add_argument("allow-running-insecure-content")
browser = webdriver.Chrome(options=options)

browser.get("http://typingsensei.com/login")

time.sleep(2)

WebDriverWait(browser, 20).until(
   EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))

cookieC = browser.find_element_by_xpath('//*[@id="app"]/section/div/button')
cookieC.click()

time.sleep(2)

## change <YOUR USERNAME HERE> to your email or username, without brackets
## change <YOUR PASSWORD HERE> to your password, without brackets

emailID = "<YOUR USERNAME HERE>"
passW = "<YOUR PASSWORD HERE>"

username = browser.find_element_by_id('email')
username.send_keys(emailID)

password = browser.find_element_by_id('password')
password.send_keys(passW)


## when there was no captcha, i just automatically ran the next code which is play1.py
## after the captcha, i manually answer it then run the code


# time.sleep(120)
# browser.close()
