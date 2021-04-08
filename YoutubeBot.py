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
import argparse
import threading

MAX_TIMEOUT = 128 # change timeout duration
#THREAD_COUNT = 1 # change no. of instances of threads to open at once
#c=1 # keep track of counts

url = random.choice(open('links.txt').readlines())
useragent = random.choice(open('useragents.txt').readlines())
proxy = random.choice(open('proxies.txt').readlines())

opts1 = Options()
opts1.add_argument('--user-agent=%s'% useragent)
#opts1.add_argument('--mute-audio')
opts1.add_argument('--incognito')
opts1.add_argument('--proxy-server=%s'% proxy)
#opts1.add_argument('--headless')
opts1.add_argument('--start-maximized')
#opts1.add_argument('--disable-gpu')
opts1.add_argument('--headless')
opts1.add_argument('--autoplay-policy=no-user-gesture-required')
opts1.add_argument('--no-sandbox')
opts1.add_argument('--disable-dev-shm-usage')
opts1.add_argument('--disk-cache-size=0')
opts1.add_argument('--disable-local-storage')
opts1.add_argument('--disable-logging')
opts1.add_argument('--enable-low-res-tiling')
driver = webdriver.Chrome(options=opts1)
#driver.set_page_load_timeout(10)
try:
    driver.get(url)
    time.sleep(MAX_TIMEOUT)
    driver.quit()
except:
    driver.quit()
finally:
    os.startfile('YoutubeBot.exe')