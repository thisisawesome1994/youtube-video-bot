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
import undetected_chromedriver as uc
import requests

FINGERPRINT = os.path.join('extension', 'fingerprint_defender.zip')
TIMEZONE = os.path.join('extension', 'spoof_timezone.zip')
#WEBRTC = os.path.join('extension', 'webrtc_control.zip')
#ACTIVE = os.path.join('extension', 'always_active.zip')
MAX_TIMEOUT = 400 # change timeout duration
#THREAD_COUNT = 1 # change no. of instances of threads to open at once
#c=1 # keep track of counts
url = random.choice(open('links.txt').readlines())
useragent = random.choice(open('useragents.txt').readlines())
proxy = random.choice(open('proxies.txt').readlines())
useragent2 = random.choice(open('useragents.txt').readlines())
proxy2 = random.choice(open('proxies.txt').readlines())

WIDTH = 0
VIEWPORT = ['2560,1440', '1920,1080', '1440,900',
            '1536,864', '1366,768', '1280,1024', '1024,768', '1280,800', '1280,720', '1400,1050', '1920,1200']

CHROME = ['{8A69D345-D564-463c-AFF1-A69D9E530F96}',
        '{8237E44A-0054-442C-B6B6-EA0509993955}',
        '{401C381F-E0DE-4B85-8BD8-3F3F14FBDA57}',
        '{4ea16ac7-fd5a-47c3-875b-dbf4a2008c20}']

opts1 = Options()
opts1.add_argument('--user-agent=%s'% useragent)
opts1.add_argument('--mute-audio')
#opts1.add_argument('--incognito')
opts1.add_argument('--proxy-server=socks5://%s'% proxy)
#opts1.add_argument('--headless')
opts1.add_argument(f"--window-size={random.choice(VIEWPORT)}")
#opts1.add_argument('--disable-gpu')
opts1.add_argument('--autoplay-policy=no-user-gesture-required')
opts1.add_argument('--no-sandbox')
opts1.add_argument('--disable-dev-shm-usage')
opts1.add_argument('--disk-cache-size=0')
opts1.add_argument('--disable-local-storage')
opts1.add_argument('--disable-logging')
opts1.add_argument('--enable-low-res-tiling')
opts1.add_experimental_option('useAutomationExtension', False)
opts1.add_extension(FINGERPRINT)
opts1.add_extension(TIMEZONE)
driver = webdriver.Chrome(options=opts1)
#driver.DesiredCapabilities.CHROME['loggingPrefs'] = {
#    'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
#driver.set_page_load_timeout(10)
try:
    driver.get(url)
    time.sleep(MAX_TIMEOUT)
    driver.quit()
except:
    driver.quit()
finally:
    driver.quit()