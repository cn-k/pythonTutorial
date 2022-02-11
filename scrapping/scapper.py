from selenium import webdriver
import time
from bs4 import BeautifulSoup
#start web browser
browser = webdriver.Firefox()
while True:
    time.sleep(1)
    browser.get("https://www.doviz.com/kripto-paralar/bitcoin")
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    btc = soup.find("div", {"class": "text-xl font-semibold text-white"})
    print(btc.contents[0])
    time.sleep(10)
browser.close()