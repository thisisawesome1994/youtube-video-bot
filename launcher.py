import time
from time import sleep
import os
from os import system,name
import subprocess

while True:
    time.sleep(20)
    subprocess.call('YoutubeBot.exe')
    subprocess.call('taskkill /F /IM YoutubeBot.exe /T')
    subprocess.call('taskkill /F /IM chromedriver.exe /T')
    subprocess.call('taskkill /F /IM chrome.exe /T')
    subprocess.call('clean.bat')