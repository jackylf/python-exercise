import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Step 1: Use requests to get a webpage
print('百度ing...')

print(sys.argv)
url = "https://www.baidu.com/s?wd=" + ' '.join(sys.argv[1:])  






