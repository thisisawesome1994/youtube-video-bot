from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from random import randint
from time import sleep
import os
import time
import random
#view_time = float(input('enter total time for all views: '))
proxy = random.choice(open('proxies.txt').readlines())
useragent = random.choice(open('useragents.txt').readlines())
url = random.choice(open('links.txt').readlines())

opts1 = Options()
opts1.add_argument('--user-agent=%s'% useragent)
#opts1.add_argument('--mute-audio')
opts1.add_argument('--incognito')
#opts1.add_argument('--headless')
opts1.add_argument('--proxy-server=%s'% proxy)
opts1.add_argument('--start-maximized')
browser1 = webdriver.Chrome(options=opts1)
browser1.get(url)
time.sleep(10)
if len(browser1.find_elements_by_xpath("//button[@class='ytp-large-play-button ytp-button']")) > 0:
    browser1.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']").click()
    time.sleep(randint(36,360))
    os.startfile("launch.exe")
    browser1.quit()
else:
    time.sleep(randint(36,360))
    os.startfile("launch.exe")
    browser1.quit()
#time.sleep(10)
#play_music_1 = browser1.find_element_by_xpath(""" //*[@id="movie_player"]/div[5]/button """)
#play_music_1.click()

# script by thisisawesome1994