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
parser = argparse.ArgumentParser()


#-db DATABSE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-c", "--cycles", help="Amount of cycles", type=int)
parser.add_argument("-t", "--min", help="Minimal Viewtime", type=int)
parser.add_argument("-m", "--max", help="Maximal Viewtime", type=int)
# parser.add_argument("-size", "--size", help="Size", type=int)

args = parser.parse_args()

for i in range(args.cycles):
    proxy1 = random.choice(open('proxies.txt').readlines())
    useragent1 = random.choice(open('useragents.txt').readlines())
    url1 = random.choice(open('links.txt').readlines())
    proxy2 = random.choice(open('proxies.txt').readlines())
    useragent2 = random.choice(open('useragents.txt').readlines())
    url2 = random.choice(open('links.txt').readlines())
    proxy3 = random.choice(open('proxies.txt').readlines())
    useragent3 = random.choice(open('useragents.txt').readlines())
    url3 = random.choice(open('links.txt').readlines())
    proxy4 = random.choice(open('proxies.txt').readlines())
    useragent4 = random.choice(open('useragents.txt').readlines())
    url4 = random.choice(open('links.txt').readlines())
    proxy5 = random.choice(open('proxies.txt').readlines())
    useragent5 = random.choice(open('useragents.txt').readlines())
    url5 = random.choice(open('links.txt').readlines())
    proxy6 = random.choice(open('proxies.txt').readlines())
    useragent6 = random.choice(open('useragents.txt').readlines())
    url6 = random.choice(open('links.txt').readlines())
    proxy7 = random.choice(open('proxies.txt').readlines())
    useragent7 = random.choice(open('useragents.txt').readlines())
    url7 = random.choice(open('links.txt').readlines())
    proxy8 = random.choice(open('proxies.txt').readlines())
    useragent8 = random.choice(open('useragents.txt').readlines())
    url8 = random.choice(open('links.txt').readlines())
    proxy9 = random.choice(open('proxies.txt').readlines())
    useragent9 = random.choice(open('useragents.txt').readlines())
    url9 = random.choice(open('links.txt').readlines())
    proxyA = random.choice(open('proxies.txt').readlines())
    useragentA = random.choice(open('useragents.txt').readlines())
    urlA = random.choice(open('links.txt').readlines())
    
    opts1 = Options()
    opts1.add_argument('--user-agent=%s'% useragent1)
    #opts1.add_argument('--mute-audio')
    opts1.add_argument('--incognito')
    opts1.add_argument('--proxy-server=%s'% proxy1)
    #opts1.add_argument('--headless')
    opts1.add_argument('--start-maximized')
    opts1.add_argument('--disable-gpu')
    opts1.add_argument('--autoplay-policy=no-user-gesture-required')
    opts1.add_argument('--no-sandbox')
    opts1.add_argument('--disable-dev-shm-usage')
    opts1.add_argument('--disk-cache-size=0')
    opts1.add_argument('--disable-local-storage')
    opts1.add_argument('--disable-logging')
    opts1.add_argument('--enable-low-res-tiling')
    
    opts2 = Options()
    opts2.add_argument('--user-agent=%s'% useragent2)
    #opts1.add_argument('--mute-audio')
    opts2.add_argument('--incognito')
    opts2.add_argument('--proxy-server=%s'% proxy2)
    #opts1.add_argument('--headless')
    opts2.add_argument('--start-maximized')
    opts2.add_argument('--disable-gpu')
    opts2.add_argument('--autoplay-policy=no-user-gesture-required')
    opts2.add_argument('--no-sandbox')
    opts2.add_argument('--disable-dev-shm-usage')
    opts2.add_argument('--disk-cache-size=0')
    opts2.add_argument('--disable-local-storage')
    opts2.add_argument('--disable-logging')
    opts2.add_argument('--enable-low-res-tiling')

    opts3 = Options()
    opts3.add_argument('--user-agent=%s'% useragent3)
    #opts1.add_argument('--mute-audio')
    opts3.add_argument('--incognito')
    opts3.add_argument('--proxy-server=%s'% proxy3)
    #opts1.add_argument('--headless')
    opts3.add_argument('--start-maximized')
    opts3.add_argument('--disable-gpu')
    opts3.add_argument('--autoplay-policy=no-user-gesture-required')
    opts3.add_argument('--no-sandbox')
    opts3.add_argument('--disable-dev-shm-usage')
    opts3.add_argument('--disk-cache-size=0')
    opts3.add_argument('--disable-local-storage')
    opts3.add_argument('--disable-logging')
    opts3.add_argument('--enable-low-res-tiling')
    
    opts4 = Options()
    opts4.add_argument('--user-agent=%s'% useragent4)
    #opts1.add_argument('--mute-audio')
    opts4.add_argument('--incognito')
    opts4.add_argument('--proxy-server=%s'% proxy4)
    #opts1.add_argument('--headless')
    opts4.add_argument('--start-maximized')
    opts4.add_argument('--disable-gpu')
    opts4.add_argument('--autoplay-policy=no-user-gesture-required')
    opts4.add_argument('--no-sandbox')
    opts4.add_argument('--disable-dev-shm-usage')
    opts4.add_argument('--disk-cache-size=0')
    opts4.add_argument('--disable-local-storage')
    opts4.add_argument('--disable-logging')
    opts4.add_argument('--enable-low-res-tiling')
    
    opts5 = Options()
    opts5.add_argument('--user-agent=%s'% useragent5)
    #opts1.add_argument('--mute-audio')
    opts5.add_argument('--incognito')
    opts5.add_argument('--proxy-server=%s'% proxy5)
    #opts1.add_argument('--headless')
    opts5.add_argument('--start-maximized')
    opts5.add_argument('--disable-gpu')
    opts5.add_argument('--autoplay-policy=no-user-gesture-required')
    opts5.add_argument('--no-sandbox')
    opts5.add_argument('--disable-dev-shm-usage')
    opts5.add_argument('--disk-cache-size=0')
    opts5.add_argument('--disable-local-storage')
    opts5.add_argument('--disable-logging')
    opts5.add_argument('--enable-low-res-tiling')
    
    opts6 = Options()
    opts6.add_argument('--user-agent=%s'% useragent6)
    #opts1.add_argument('--mute-audio')
    opts6.add_argument('--incognito')
    opts6.add_argument('--proxy-server=%s'% proxy6)
    #opts1.add_argument('--headless')
    opts6.add_argument('--start-maximized')
    opts6.add_argument('--disable-gpu')
    opts6.add_argument('--autoplay-policy=no-user-gesture-required')
    opts6.add_argument('--no-sandbox')
    opts6.add_argument('--disable-dev-shm-usage')
    opts6.add_argument('--disk-cache-size=0')
    opts6.add_argument('--disable-local-storage')
    opts6.add_argument('--disable-logging')
    opts6.add_argument('--enable-low-res-tiling')
    
    opts7 = Options()
    opts7.add_argument('--user-agent=%s'% useragent7)
    #opts1.add_argument('--mute-audio')
    opts7.add_argument('--incognito')
    opts7.add_argument('--proxy-server=%s'% proxy7)
    #opts1.add_argument('--headless')
    opts7.add_argument('--start-maximized')
    opts7.add_argument('--disable-gpu')
    opts7.add_argument('--autoplay-policy=no-user-gesture-required')
    opts7.add_argument('--no-sandbox')
    opts7.add_argument('--disable-dev-shm-usage')
    opts7.add_argument('--disk-cache-size=0')
    opts7.add_argument('--disable-local-storage')
    opts7.add_argument('--disable-logging')
    opts7.add_argument('--enable-low-res-tiling')
    
    opts8 = Options()
    opts8.add_argument('--user-agent=%s'% useragent8)
    #opts1.add_argument('--mute-audio')
    opts8.add_argument('--incognito')
    opts8.add_argument('--proxy-server=%s'% proxy8)
    #opts1.add_argument('--headless')
    opts8.add_argument('--start-maximized')
    opts8.add_argument('--disable-gpu')
    opts8.add_argument('--autoplay-policy=no-user-gesture-required')
    opts8.add_argument('--no-sandbox')
    opts8.add_argument('--disable-dev-shm-usage')
    opts8.add_argument('--disk-cache-size=0')
    opts8.add_argument('--disable-local-storage')
    opts8.add_argument('--disable-logging')
    opts8.add_argument('--enable-low-res-tiling')
    
    opts9 = Options()
    opts9.add_argument('--user-agent=%s'% useragent9)
    #opts1.add_argument('--mute-audio')
    opts9.add_argument('--incognito')
    opts9.add_argument('--proxy-server=%s'% proxy9)
    #opts1.add_argument('--headless')
    opts9.add_argument('--start-maximized')
    opts9.add_argument('--disable-gpu')
    opts9.add_argument('--autoplay-policy=no-user-gesture-required')
    opts9.add_argument('--no-sandbox')
    opts9.add_argument('--disable-dev-shm-usage')
    opts9.add_argument('--disk-cache-size=0')
    opts9.add_argument('--disable-local-storage')
    opts9.add_argument('--disable-logging')
    opts9.add_argument('--enable-low-res-tiling')
    
    optsA = Options()
    optsA.add_argument('--user-agent=%s'% useragentA)
    #opts1.add_argument('--mute-audio')
    optsA.add_argument('--incognito')
    optsA.add_argument('--proxy-server=%s'% proxyA)
    #opts1.add_argument('--headless')
    optsA.add_argument('--start-maximized')
    optsA.add_argument('--disable-gpu')
    optsA.add_argument('--autoplay-policy=no-user-gesture-required')
    optsA.add_argument('--no-sandbox')
    optsA.add_argument('--disable-dev-shm-usage')
    optsA.add_argument('--disk-cache-size=0')
    optsA.add_argument('--disable-local-storage')
    optsA.add_argument('--disable-logging')
    optsA.add_argument('--enable-low-res-tiling')

    browser1 = webdriver.Chrome(options=opts1)
    browser2 = webdriver.Chrome(options=opts2)
    browser3 = webdriver.Chrome(options=opts3)
    browser4 = webdriver.Chrome(options=opts4)
    browser5 = webdriver.Chrome(options=opts5)
    browser6 = webdriver.Chrome(options=opts6)
    browser7 = webdriver.Chrome(options=opts7)
    browser8 = webdriver.Chrome(options=opts8)
    browser9 = webdriver.Chrome(options=opts9)
    browserA = webdriver.Chrome(options=optsA)
    browser1.get(url1)
    browser2.get(url2)
    browser3.get(url3)
    browser4.get(url4)
    browser5.get(url5)
    browser6.get(url6)
    browser7.get(url7)
    browser8.get(url8)
    browser9.get(url9)
    browser1.get(urlA)
    time.sleep(randint(args.min, args.max))
    browser1.quit()

# script by thisisawesome1994
