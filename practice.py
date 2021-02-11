from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import random


def send_delayed_keys(element, text, delay) :
    for c in text :
        endtime = time.time() + delay
        element.send_keys(c)
        time.sleep(abs(endtime - time.time()))
        
keyDelay = random.uniform(0,0.2)


browser = webdriver.Chrome()
browser.get("http://typingsensei.com/login")

# browser = webdriver.Chrome()

emailID = "mikaela2000@macr2.com"
passW = "mika1128"


# fill in username and hit the next button

username = browser.find_element_by_id('email')
username.send_keys(emailID)

password = browser.find_element_by_id('password')
password.send_keys(passW)

nextButton = browser.find_element_by_xpath('//*[@id="app"]/main/div/section/section/form/div[4]/button')
nextButton.click()

browser.implicitly_wait(5)

#load second page after login
browser.get("http://typingsensei.com/training-dojo")
display = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/section/span[1]')))

playNow = browser.find_element_by_xpath('//*[@id="app"]/main/div/section/div[3]/button')
browser.implicitly_wait(7)
playNow.click()

browser.implicitly_wait(5)

# need to loop here

timer = browser.find_element_by_xpath('//*[@id="app"]/main/div/section/div[2]/div[2]/span[1]').text

while timer != "00:05":
    time.sleep(1)
    wordID = browser.find_element_by_xpath('//*[@id="word"]')
    typeme = wordID.get_attribute("data-word")

    # fill in username and hit the next button
    entry = browser.find_element_by_id('typing-dojo')
    #entry.send_keys(typeme)
    send_delayed_keys(entry,typeme,keyDelay)

    
    


