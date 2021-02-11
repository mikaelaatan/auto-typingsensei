from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import random
import pickle


def send_delayed_keys(element, text, delay) :
    for c in text :
        # endtime = time.time() + delay
        element.send_keys(c)
        time.sleep(delay)
    
def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d:%02d:%02d" % (hour, min, sec)


options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=selenium1')
options.add_argument('ignore-certificate-errors')
options.add_experimental_option("detach", True)
options.add_argument("enable-javascript")
options.add_argument("--enable-file-cookies")
options.add_argument("allow-scripts")
options.add_argument("allow-running-insecure-content")
browser = webdriver.Chrome(options=options)

browser.get('http://typingsensei.com/play')
time.sleep(3)

################### NO 1 HOUR LOOP ############################
# t_end = time.time() + 110
# while time.time() < t_end:
#     keyDelay = random.uniform(0,0.185)
#     time.sleep(0.5)
#     wordID = browser.find_element_by_xpath('//*[@id="word"]')
#     typeme = wordID.get_attribute("data-word")
#     # fill in typing word
#     entry = browser.find_element_by_xpath('//*[@id="typing-dojo"]')
#     send_delayed_keys(entry,typeme,keyDelay)
# time.sleep(10)
# WebDriverWait(browser, 30).until(
#    EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/main/div/section[1]/span/p')))
# time.sleep(10)

 
# WILL LOOP CONTINUALLY HERE
while True:    
    ## CLICK THE PLAY BUTTON
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div/main/div/section[1]/div[2]/button')))

    playNow = browser.find_element_by_xpath('/html/body/div/main/div/section[1]/div[2]/button')
    playNow.click()

    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="typing-dojo"]')))

    ## WILL TRACK THE TIME HERE
    t_end = time.time() + 110
    while time.time() < t_end:
        keyDelay = random.uniform(0,0.185)
        time.sleep(0.5)

        ## GET THE WORD TO BE TYPED
        wordID = browser.find_element_by_xpath('//*[@id="word"]')
        typeme = wordID.get_attribute("data-word")

        # FILL IN THE WORD TO BE TYPED
        entry = browser.find_element_by_xpath('//*[@id="typing-dojo"]')
        send_delayed_keys(entry,typeme,keyDelay)

    ## AFTER 2 MINUTES WAIT FOR LOADING AND CONFIRMATION
    WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/main/div/section[1]/span/p')))

    randomSeconds = random.randint(180,1000)
    totalSeconds = (3600+randomSeconds)

    waitTime = convert(totalSeconds)
    print("Total wait time: " + str(waitTime))
    time.sleep(totalSeconds)