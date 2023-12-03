import bs4
from selenium import webdriver

browser = webdriver.Edge()
browser.get('https://www.weather.gov/riw/')
c = browser.page_source

soup = bs4.BeautifulSoup(c, 'html.parser')
all = soup.find_all('span', {'id': 'myfcst-tempf'})
print(all[0].text)


browser.quit()