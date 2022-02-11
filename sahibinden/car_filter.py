from selenium import webdriver
import time
from bs4 import BeautifulSoup
import sahibinden.car as c
import sahibinden.repository.pg as pg
import math

# start web browser
browser = webdriver.Firefox()

url = "https://www.sahibinden.com/otomobil?date=30days"
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
cars = soup.findAll("tr", {"class": "searchResultsItem"})
result_text = soup.find("div", {"class": "result-text"})
result_item_size = int(result_text.findAll('span')[1].contents[0].split(' ')[0].replace('.', ''))
iteration_size = math.ceil(result_item_size / 20)
for i in range(iteration_size):
    if i > 0:
        browser.get(url + f"&pagingOffset={i*20}")
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        cars = soup.findAll("tr", {"class": "searchResultsItem"})
    car_list = []
    for car in cars:
        if car.has_attr('data-id'):
            data_id = car['data-id']
            searchResultsLargeThumbnail = car.find("td", {"class": "searchResultsLargeThumbnail"})
            a = car.find("a")
            href = a['href']
            img = a.find('img')
            src = img['src']

            searchResultsTagAttributeValue = car.findAll('td', {'class': 'searchResultsTagAttributeValue'})
            brand = searchResultsTagAttributeValue[0].contents[0].text.replace('\n', '').strip()
            model = searchResultsTagAttributeValue[1].contents[0].text.replace('\n', '').strip()
            package = searchResultsTagAttributeValue[2].contents[0].text.replace('\n', '').strip()

            searchResultsAttributeValue = car.findAll('td', {'class': 'searchResultsAttributeValue'})
            year = int(searchResultsAttributeValue[0].contents[0].text.replace('\n', '').strip())
            km = searchResultsAttributeValue[1].contents[0].text.replace('\n', '').strip()
            color = searchResultsAttributeValue[2].contents[0].text.replace('\n', '').strip()
            searchResultsPriceValue = car.findAll('td', {'class': 'searchResultsPriceValue'})
            price = searchResultsPriceValue[0].find('div').contents[0].text.strip()
            my_car = c.Car(data_id, brand, model, package, year, km, color, price, href, src)
            car_list.append(my_car)
    pg.car_insert(car_list)
    car_list.clear()
    time.sleep(2)
browser.close()