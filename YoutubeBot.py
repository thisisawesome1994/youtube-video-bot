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

    browser1 = webdriver.Chrome(options=opts1)
    browser1.execute_script("window.location.replace(arguments[0])", url1)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", url2)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", url3)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", url4)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", url5)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", url6)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", url7)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", url8)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", url9)
    time.sleep(randint(args.min, args.max))
    browser1.execute_script("window.location.replace(arguments[0])", urlA)
    time.sleep(randint(args.min, args.max))
    browser1.quit()

# script by thisisawesome1994
