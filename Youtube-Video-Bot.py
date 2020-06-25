from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
import time
import random
views = int(input("enter no. of view: "))
cycle_time = float(input('Enter time for each view:'))
#view_time = float(input('enter total time for all views: '))
proxy = random.choice(open('proxies.txt').readlines())
useragent = random.choice(open('useragents.txt').readlines())

for i in range(views):
    opts1 = Options()
    opts1.add_argument('--user-agent=%s'% useragent)
#opts1.add_argument('--mute-audio')
opts1.add_argument('--incognito')
#opts1.add_argument('--headless')
opts1.add_argument('--proxy-server=%s'% proxy)
opts1.add_argument('--start-maximized')
browser1 = webdriver.Chrome(options=opts1)
with open('links.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for url in lines:
    browser1.get(url)
    time.sleep(cycle_time)
browser1.quit()
#time.sleep(10)
#play_music_1 = browser1.find_element_by_xpath(""" //*[@id="movie_player"]/div[5]/button """)
#play_music_1.click()

# script by thisisawesome1994