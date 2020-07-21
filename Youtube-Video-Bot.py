from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from random import randint
from time import sleep
import time
import os
import random

loop_time = int(input("Enter time to run the bot"))
views = int(input("Enter amount of loops"))

for i in range(views):
    proxy = random.choice(open('proxies.txt').readlines())
    useragent = random.choice(open('useragents.txt').readlines())
    url = random.choice(open('links.txt').readlines())

    opts1 = Options()
    opts1.add_argument('--user-agent=%s'% useragent)
    #opts1.add_argument('--mute-audio')
    opts1.add_argument('--incognito')
    opts1.add_argument('--proxy-server=%s'% proxy)
    #opts1.add_argument('--headless')
    opts1.add_argument('--start-maximized')
    opts1.add_argument('--disable-gpu')

    browser1 = webdriver.Chrome(options=opts1)
    
    browser1.execute_script("window.location.replace(arguments[0])", url)
    #if ytplay.is_displayed():
#    ytplay.click()
#    print("Starting...")
#    else ytplay.click()
    time.sleep(12)
    browser1.minimize_window()
    time.sleep(loop_time)
#aria_valuenow = browser1.find_element_by_css_selector('span').get_attribute("aria-valuenow")
#next_button = browser1.find_element_by_xpath(""" //*[@id="left-controls"]/div/paper-icon-button[3] """)
#playback = aria-value="89"
#time.sleep(wait)
    browser1.close()
#try:
#    element_next = WebDriverWait(browser1, 100).until(
#        EC.visibility_of_element_located((By.CSS_SELECTOR, 'aria-valuenow=89'))
#    )
#finally:
    


#if ():
#    next_button.click()
#    else browser1.close()
#time.sleep(randint(180,3200))
#browser1.close()


# script by thisisawesome1994
